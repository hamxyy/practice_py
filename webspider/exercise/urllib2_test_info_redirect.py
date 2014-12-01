'''
Created on 29 May, 2014

@author: z0037v8z
'''
import proxy
from urllib2 import Request, urlopen, URLError, HTTPError

old_url = "http://rrurl.cn/b1UZuP"
req = Request(old_url)
response = urlopen(req)
print "Old url: " + old_url
print "New url: " + response.geturl()

req = Request("http://www.baidu.com/")
response = urlopen(req)
print "Info: "
print response.info()