import urllib2
import proxy
import cookielib  

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie), proxy.proxy_handler())
response = opener.open("http://player.kuwo.cn/MUSIC/#")

for item in cookie:  
    print 'Name = ' + item.name  
    print 'Value = ' + item.value

print "Done"