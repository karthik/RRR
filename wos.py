
# coding: utf-8

# In[1]:

from suds.client import Client
from suds.transport.http import HttpTransport
import urllib2
from suds.sudsobject import asdict
import json
import time


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

    def search(self, query, count):
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
            }],
            'timeSpan' : {
                'begin' : '2000-01-01',
                'end'   : '2014-12-31'
            }
        }
        rparams = {
            'count' : count, # 1-100
            'firstRecord' : 1,
            #'fields' : [{
            #    'name' : 'Relevance',
            #    'sort' : 'D',
            #}],
        }
        return self.client['search'].service.search(qparams, rparams)
    
    def retrieve(self, queryId, firstRecord, count):
        rparams = {
            'count' : count, # 1-100
            'firstRecord' : firstRecord,
        }
        return self.client['search'].service.retrieve(queryId, rparams)


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

def searchAndDumpResults(term, count = 100):
    query = 'ts=' + term
    results = soap.search(query, count = count)
    queryId = results.queryId
    numRecords = results.recordsFound
    print 'search topic: ' + term
    print `numRecords` + ' records found'
    
    filename = 'data/' + term + '.json'
    with open(filename, 'w') as outf:
        json.dump(recursive_asdict(results), outf)
        
    percent = -1
    for i in xrange(1, numRecords/count+1):
        newPercent = int(100*count*i/(numRecords*1.0))
        if(newPercent != percent):
            percent = newPercent
            print `percent` + ' %'
        
        time.sleep(0.5)
        results = soap.retrieve(queryId = queryId, firstRecord = count*i+1, count = count)
        
        with open(filename, 'a') as outf:
            json.dump(recursive_asdict(results), outf)
    


# In[6]:

soap = WokmwsSoapClient()


# In[7]:

RRRterms = ['reproducibility', 'replicability', 'repeatability']


# In[8]:

for term in RRRterms:
    searchAndDumpResults(term)


# In[188]:

#results = soap.search('au=hallam', count = count)
#results = soap.search('ts=reproducibility', count = count)

#queryId = results.queryId
#numRecords = results.recordsFound
#print results.recordsFound

#with open('out.json', 'w') as outf:
#    json.dump(recursive_asdict(results), outf)

#for i in xrange(1, numRecords/count+1):
#    time.sleep(1)
#    print `round(100*count*i/(numRecords*1.0))` + '%'
#    results = soap.retrieve(queryId = queryId, firstRecord = count*i+1, count = count)
#    with open('out.json', 'a') as outf:
#        json.dump(recursive_asdict(results), outf)

#print results.recordsFound
#print queryId
#print results
#dir(results)
#suds_to_json(results)


# In[19]:

if(1 != 1):
    print 1


# In[ ]:



