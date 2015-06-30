
# coding: utf-8

# In[1]:

from suds.client import Client
from suds.transport.http import HttpTransport
import urllib2
from suds.sudsobject import asdict
import json


# In[2]:

class HTTPSudsPreprocessor(urllib2.BaseHandler):
    def __init__(self, SID):
        self.SID = SID

    def http_request(self, req):
        req.add_header('cookie', 'SID="'+self.SID+'"')
        return req

    https_request = http_request


# In[3]:

class WokmwsSoapClient():
    """
    main steps you have to do:
        soap = WokmwsSoapClient()
        results = soap.search(...)
    """
    def __init__(self):
        self.url = self.client = {}
        self.SID = ''

        #self.url['auth'] = 'http://search.isiknowledge.com/esti/wokmws/ws/WOKMWSAuthenticate?wsdl'
        self.url['auth'] = 'http://search.webofknowledge.com/esti/wokmws/ws/WOKMWSAuthenticate?wsdl'
        #self.url['search'] = 'http://search.isiknowledge.com/esti/wokmws/ws/WokSearchLite?wsdl'
        self.url['search'] = 'http://search.webofknowledge.com/esti/wokmws/ws/WokSearchLite?wsdl'

        self.prepare()

    def __del__(self):
        self.close()

    def prepare(self):
        """does all the initialization we need for a request"""
        self.initAuthClient()
        self.authenticate()
        self.initSearchClient()

    def initAuthClient(self):
        self.client['auth'] = Client(self.url['auth'])

    def initSearchClient(self):
        http = HttpTransport()
        opener = urllib2.build_opener(HTTPSudsPreprocessor(self.SID))
        http.urlopener = opener
        self.client['search'] = Client(self.url['search'], transport = http)

    def authenticate(self):
        self.SID = self.client['auth'].service.authenticate()

    def close(self):
        self.client['auth'].service.closeSession()

    def search(self, query):
        qparams = {
            'databaseId' : 'WOS',
            'userQuery' : query,
            'queryLanguage' : 'en',
            'editions' : [{
                'collection' : 'WOS',
                'edition' : 'SCI',
            },{
                'collection' : 'WOS',
                'edition' : 'SSCI',
            }]
        }

        rparams = {
            'count' : 5, # 1-100
            'firstRecord' : 1,
            #'fields' : [{
            #    'name' : 'Relevance',
            #    'sort' : 'D',
            #}],
        }

        return self.client['search'].service.search(qparams, rparams)


# In[4]:

def recursive_asdict(d):
    """Convert Suds object into serializable format."""
    out = {}
    for k, v in asdict(d).iteritems():
        if hasattr(v, '__keylist__'):
            out[k] = recursive_asdict(v)
        elif isinstance(v, list):
            out[k] = []
            for item in v:
                if hasattr(item, '__keylist__'):
                    out[k].append(recursive_asdict(item))
                else:
                    out[k].append(item)
        else:
            out[k] = v
    return out

def suds_to_json(data):
    return json.dumps(recursive_asdict(data))


# In[5]:

soap = WokmwsSoapClient()


# In[6]:

results = soap.search('AU=Hallam')

with open('out.json', 'w') as outf:
    json.dump(recursive_asdict(results), outf)


# In[7]:

#print results.recordsFound
#print results
#dir(results)
#suds_to_json(results)

