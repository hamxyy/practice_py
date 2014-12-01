'''
Created on 29 May, 2014

@author: z0037v8z
'''

# -*- coding: utf-8 -*-  
import proxy
import urllib  
import urllib2  
postdata=urllib.urlencode({  
    'username':'hamxyy',  
    'password':'why888',  
    'continueURI':'http://www.verycd.com/',  
    'fk':'',  
    'login_submit':'login'  
})  
req = urllib2.Request(  
    url = 'http://secure.verycd.com/signin',  
    data = postdata  
)  
result = urllib2.urlopen(req)  
print result.read()   