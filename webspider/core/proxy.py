'''
Created on 29 May, 2014

@author: z0037v8z
'''
import urllib2

def proxy_handler():
    return urllib2.ProxyHandler({"http":"http://10.50.80.50:8080"})

def install():
    proxy_support = proxy_handler()
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    
install()