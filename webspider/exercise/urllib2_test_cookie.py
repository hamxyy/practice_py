'''
Created on 29 May, 2014

@author: z0037v8z
'''

import proxy
import urllib2
import cookielib  

cookie = cookielib.CookieJar()  
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie), proxy.proxy_handler())  
response = opener.open('http://www.baidu.com')
i = 0
for item in cookie:  
    print 'Name = ' + item.name  
    print 'Value = ' + item.value
    i += 1
    if(i >= 10):
        break
