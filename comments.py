import httplib, urllib 
from bs4 import BeautifulSoup 
import os 
import json
import time

access_token='EAAi4Va5lVxIBAFcPkJLCTW2Pdl5OfNBpG8qqVDchLxRVDVP4dp9HU4RgfRjNBoQc0yGxPZAZAEeZClwaFZBZCp0IZCCoA9M6hCl7r5DxalVWkvBjkOtbTZAlALYR6gDjM14voiu67QPZBOgwy8mVQxksTvLdHkkWn8jQDR113yZA3VPwZCObjaSQT8i8DmWIWS5swZAgshUj7l7OwZDZD'
# access_token = raw_input('EAAi4Va5lVxIBAFcPkJLCTW2Pdl5OfNBpG8qqVDchLxRVDVP4dp9HU4RgfRjNBoQc0yGxPZAZAEeZClwaFZBZCp0IZCCoA9M6hCl7r5DxalVWkvBjkOtbTZAlALYR6gDjM14voiu67QPZBOgwy8mVQxksTvLdHkkWn8jQDR113yZA3VPwZCObjaSQT8i8DmWIWS5swZAgshUj7l7OwZDZD')

conn = httplib.HTTPSConnection("graph.facebook.com") 
print 'Please Wait!'
 
def comment(url): 
    connect = httplib.HTTPSConnection("graph.facebook.com") 
    connect.request("GET",url) 
    for x in xrange(7000000): 
            
            print 'commenting %d '% x
            path ='/'+'2326459350710288'+'/comments'
            param_data={  'format':'json', 
                        'Hola':'<3', 
                        'access_token':access_token 
                  } 
            connect = httplib.HTTPSConnection("graph.facebook.com") 
            connect.request("POST",path,urllib.urlencode(param_data),{}) 
            time.sleep(0.09)
           
url='/2326459350710288' 
comment(url) 
print 'DONE!'
