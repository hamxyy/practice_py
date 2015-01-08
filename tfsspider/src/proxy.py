'''
Created on 29 May, 2014

@author: z0037v8z
'''
import urllib2

proxy = urllib2.ProxyHandler({'http': '10.50.34.35:84'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)