---
title: "Reproducibility Lexicon"
author: "Karthik Ram"
date: "May 1, 2015"
output: html_document
---






```r
library(dplyr)
library(ggplot2)
library(wesanderson)
library(readr)
library(pander)
```


```r
files <- paste0("parsed/", dir('parsed'))
# Three files so far
files
```

```
#> [1] "parsed/Repeatibility.csv"   "parsed/Replicability.csv"  
#> [3] "parsed/Reproducibility.csv"
```

# Repeatibility


```r
r1 <- read_csv(file = files[1])
r2 <- r1 %>% select(-AB)
pandoc.table(head(r2))
```


------------------------------------------------------------------
 PT                AU                             TI              
---- ------------------------------ ------------------------------
 J     Panseri, SaraChiesa, Luca      Improved determination of   
            MariaBrizzolari,               malonaldehyde by       
           AndreaSantaniello,              high-performance       
     EnzoPassero, ElenaBiondi, Pier  liquidchromatography with UV 
     Antonio                                 detection as         
                                        2,3-diaminonaphthalene    
                                         derivative               

 J     Hazra, A.Dutta, K.Bhowmik,     Highly Repeatable Low-ppm   
     B.Bhattacharyya, Partha               Ethanol Sensing        
                                    Characteristics ofp-TiO2-Based
                                    Resistive Devices             

 J      Bonanno, GiovanniMarano,    Characterization Measurements 
             DavideBelluso,          Methodology and Instrumental 
         MassimilianoBillotta,        Set-UpOptimization for New  
             SergioGrillo,              SiPM Detectors-Part I:    
           AlessandroGarozzo,       Electrical Tests              
            SalvatoreRomeo,                                       
        GiuseppeTimpanaro, Maria                                  
                Cristina                                          

 J      Bonanno, GiovanniMarano,    Characterization Measurements 
             DavideBelluso,          Methodology and Instrumental 
         MassimilianoBillotta,        Set-UpOptimization for New  
             SergioGrillo,             SiPM Detectors-Part II:    
           AlessandroGarozzo,       Optical Tests                 
            SalvatoreRomeo,                                       
        GiuseppeTimpanaro, Maria                                  
                Cristina                                          

 J   Yibar, ArtunOzcan, AliKaraca,  Determination of Erythromycin,
     Mehmet Yilmaz                    Spiramycin, Tilmicosin and  
                                    Tylosin inAnimal Feedingstuffs
                                              by Liquid           
                                      Chromatography-Tandem Mass  
                                         Spectrometry             

 J    Pinto, F. S. T.Fogliatto, F.     A method for panelists'    
     S.Qannari, E. M.                 consistency assessment in   
                                     sensory evaluationsbased on  
                                         the Cronbach's alpha     
                                    coefficient                   
------------------------------------------------------------------

Table: Table continues below

 
------------------------------------------------------------------
              SO                             DI                PY 
------------------------------ ------------------------------ ----
  JOURNAL OF CHROMATOGRAPHY    10.1016/j.jchromb.2014.11.017  2015
 B-ANALYTICAL TECHNOLOGIES IN                                     
    THE BIOMEDICALAND LIFE                                        
           SCIENCES                                               

     IEEE SENSORS JOURNAL        10.1109/JSEN.2014.2345575    2015

     IEEE SENSORS JOURNAL        10.1109/JSEN.2014.2328621    2014

     IEEE SENSORS JOURNAL        10.1109/JSEN.2014.2328623    2014

KAFKAS UNIVERSITESI VETERINER     10.9775/kvfd.2013.10365     2014
FAKULTESI DERGISI                                                 

 FOOD QUALITY AND PREFERENCE   10.1016/j.foodqual.2013.06.006 2014
------------------------------------------------------------------


```r
counts <- r1 %>% group_by(SO) %>% 
            summarise(n = n()) %>% 
            arrange(desc(n)) %>% 
            head

pandoc.table(counts)
```


--------------------------------
             SO               n 
---------------------------- ---
JOURNAL OF CHROMATOGRAPHY A   8 

  Journal of Instrumental     5 
          Analysis              

    IEEE SENSORS JOURNAL      3 

          TALANTA             3 

ANALYTICAL AND BIOANALYTICAL  2 
         CHEMISTRY              

       Acta Amazonica         2 
--------------------------------

---

# Replicability


```r
r1 <- read_csv(file = files[2])
r2 <- r1 %>% select(-AB)
pandoc.table(head(r2))
```


------------------------------------------------------------------
 PT                AU                             TI              
---- ------------------------------ ------------------------------
 J   Usselman, Melvyn C.Brown, Todd   Atomic Theory and Multiple  
     A.                               Combining Proportions: The  
                                    Search for WholeNumber Ratios 
                                      Essay in Honour of Alan J.  
                                    Rocke                         

 J    Peng, ChanghaiHuang, LuLiu,        Design and practical     
     JianxunHuang, Ying              application of an innovative 
                                      net-zero energy housewith   
                                     integrated photovoltaics: a  
                                        case study from Solar     
                                    Decathlon China2013           

 J   Mahmood, Syed ImranDaim, Syed  The transferability of Western
         AbdulBorleffs, Jan C.       concepts to other cultures:  
           C.Heijne-Penninga,              Validation ofthe       
       MarjoleinSchonrock-Adema,    Zuckerman-Kuhlman Personality 
     Johanna                           Questionnaire in a Saudi   
                                    Arabiccontext                 

 J       He, MeianXu, MinZhang,      Meta-analysis of genome-wide 
      BenLiang, JunChen, PengLee,    association studies of adult 
     Jong-YoungJohnson, Todd A.Li,       height in EastAsians     
        HuaixingYang, XiaoboDai,    identifies 17 novel loci      
       JunchengLiang, LimingGui,                                  
         LixuanQi, QibinHuang,                                    
     JinyanLi, YanpingAdair, Linda                                
      S.Aung, TinCai, QiuyinCheng,                                
      Ching-YuCho, Myeong-ChanCho,                                
        Yoon ShinChu, MinjieCui,                                  
     BinGao, Yu-TangGo, Min JinGu,                                
        DongfengGu, WeiqiongGuo,                                  
     HuanHao, YongchenHong, JieHu,                                
        ZhibinHu, YanlingHuang,                                   
     JianfengHwang, Joo-YeonIkram,                                
          Mohammad KamranJin,                                     
       GuangfuKang, Dae-HeeKhor,                                  
      Chiea ChuenKim, Bong-JoKim,                                 
       Hung TaeKubo, MichiakiLee,                                 
       JeannetteLee, JuyoungLee,                                  
        Nanette R.Li, RuoyingLi,                                  
         JunLiu, JianJunLonge,                                    
            JirongLu, WeiLu,                                      
     XiangfengMiao, XiaopingOkada,                                
     YukinoriOng, Rick Twee-HeeQiu,                               
       GaokunSeielstad, MarkSim,                                  
     XuelingSong, HuaidongTakeuchi,                               
            FumihikoTanaka,                                       
     ToshihiroTaylor, Phil R.Wang,                                
       LaiyuanWang, WeiqingWang,                                  
      YiqinWu, ChenWu, YingXiang,                                 
      Yong-BingYamamoto, KenYang,                                 
        HandongLiao, MingYokota,                                  
      MitsuhiroYoung, TerriZhang,                                 
       XiaominKato, NorihiroWang,                                 
       Qing K.Zheng, WeiHu, Frank                                 
          B.Lin, DongxinShen,                                     
        HongbingTeo, Yik YingMo,                                  
       ZengnanWong, Tien YinLin,                                  
        XuMohlke, Karen L.Ning,                                   
      GuangTsunoda, TatsuhikoHan,                                 
      Bok-GheeShu, Xiao-OuTai, E.                                 
        ShyongWu, TangchunQi, Lu                                  

 J       Savalei, VictoriaDunn,         Is the call to abandon    
     Elizabeth                       p-values the red herring of  
                                    the replicabilitycrisis?      

 J     Ladas, Aristea I.Carroll,       Attentional Processes in   
     Daniel J.Vivas, Ana B.            Low-Socioeconomic Status   
                                     Bilingual Children:Are They  
                                      Modulated by the Amount of  
                                    Bilingual Experience?         
------------------------------------------------------------------

Table: Table continues below

 
---------------------------------------------------------------
             SO                           DI                PY 
---------------------------- ----------------------------- ----
     ANNALS OF SCIENCE       10.1080/00033790.2015.1007522 2015

ARCHITECTURAL SCIENCE REVIEW 10.1080/00038628.2015.1011075 2015

      MEDICAL TEACHER        10.3109/0142159X.2015.1006606 2015

  HUMAN MOLECULAR GENETICS        10.1093/hmg/ddu583       2015

  FRONTIERS IN PSYCHOLOGY      10.3389/fpsyg.2015.00245    2015

     CHILD DEVELOPMENT                    NA               2015
---------------------------------------------------------------


```r
counts <- r1 %>% group_by(SO) %>% 
            summarise(n = n()) %>% 
            arrange(desc(n)) %>% 
            head

pandoc.table(counts)
```


---------------------------------
             SO                n 
----------------------------- ---
             NA               51 

     EUROPEAN JOURNAL OF      27 
         PERSONALITY             

PERSPECTIVES ON PSYCHOLOGICAL 20 
           SCIENCE               

          PLOS ONE            18 

 PERSONALITY AND INDIVIDUAL   12 
         DIFFERENCES             

Contracting for agricultural  10 
extenison: international case    
studies andemerging practices    
---------------------------------

# Reproducibility


```r
r1 <- read_csv(file = files[3])
r2 <- r1 %>% select(-AB)
pandoc.table(head(r2))
```


-----------------------------------
 PT                AU              
---- ------------------------------
 J    Riyahi-Alam, SadjadHaghgoo,  
             SoheilaGorji,         
     EnsiehRiyahi-Alam, Nader      

 J      Kistler, James OPesaro,    
     ManuelWade, William G         

 J            Turci, Aline         
       MendoncaBevilaqua-Grossi,   
         DeboraPinheiro, Carina    
       FerreiraBragatto, Marcela   
      MendesChaves, Thais Cristina 

 J       Jozwiak, MarekRychlik,    
      MichalMusielak, BartoszChen, 
          Brian Po-JungIdzior,     
     MaciejGrzegorzewski, Andrzej  

 J       Weinhold, ArneWielsch,    
      NatalieSvatos, AlesBaldwin,  
     Ian T                         

 J   van Tonder, AletJoubert, Annie
     MCromarty, A Duncan           
-----------------------------------

Table: Table continues below

 
-----------------------------------------------------------
                            TI                             
-----------------------------------------------------------
                  Size Reproducibility of                  
                  Gadolinium Oxide Based                   
                 Nanomagnetic Particlesfor                 
                Cellular Magnetic Resonance                
                    Imaging: Effects of                    
              Functionalization,Chemisorption              
              and Reaction Conditions                      

              Development and pyrosequencing               
               analysis of an in-vitro oral                
              biofilmmodel.                                

                 The Brazilian Portuguese                  
                  version of the revised                   
                 Maastricht UpperExtremity                 
                  Questionnaire (MUEQ-Br                   
                  revised): translation,                   
                 cross-culturaladaptation,                 
                reliability, and structural                
                        validation.                        

                   An accurate method of                   
                radiological assessment of                 
                     acetabular volume                     
                andorientation in computed                 
                    tomography spatial                     
              reconstruction.                              

                 Label-free nanoUPLC-MS(E)                 
                  based quantification of                  
              antimicrobial peptidesfrom the               
                leaf apoplast of Nicotiana                 
              attenuata.                                   

                      Limitations of                       
the3-(4,5-dimethylthiazol-2-yl)-2,5-diphenyl-2H-tetrazolium
                  bromide (MTT)assay when                  
                compared to three commonly                 
              used cell enumeration assays.                
-----------------------------------------------------------

Table: Table continues below

 
-------------------------------------------------------------
              SO                          DI              PY 
------------------------------ ------------------------- ----
      IRANIAN JOURNAL OF                  NA             2015
PHARMACEUTICAL RESEARCH                                      

       BMC microbiology        10.1186/s12866-015-0364-1 2015

BMC musculoskeletal disorders  10.1186/s12891-015-0497-2 2015

BMC musculoskeletal disorders  10.1186/s12891-015-0503-8 2015

      BMC plant biology        10.1186/s12870-014-0398-9 2015

      BMC research notes       10.1186/s13104-015-1000-8 2015
-------------------------------------------------------------


```r
counts <- r1 %>% group_by(SO) %>% 
            summarise(n = n()) %>% 
            arrange(desc(n)) %>% 
            head

pandoc.table(counts)
```


-------------------------------
            SO               n 
--------------------------- ---
            NA              392

BIOSENSORS & BIOELECTRONICS 146

    AMERICAN JOURNAL OF     141
       ROENTGENOLOGY           

JOURNAL OF CHROMATOGRAPHY A 129

         PLOS ONE           115

   SENSORS AND ACTUATORS    102
        B-CHEMICAL             
-------------------------------
  
  
  
