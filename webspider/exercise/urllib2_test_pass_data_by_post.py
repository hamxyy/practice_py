'''
Created on 29 May, 2014

@author: z0037v8z
'''
import urllib
import urllib2
import proxy

url = "http://www.someserver.com/register.cgi"

values = {"name" : "WHY",
          "location" : "SDU",
          "language" : "Python"}

data = urllib.urlencode(values) #encode
req = urllib2.Request(url, data) #send request with data form

response = urllib2.urlopen(req) #receive message
the_page = response.read()

print the_page