'''
Created on 29 May, 2014

@author: z0037v8z
'''
import urllib2

req = urllib2.Request('http://www.baibai.com')  
  
try: urllib2.urlopen(req)  
  
except urllib2.URLError, e:    
    print e.reason