'''
Createdon08Dec,2014

@author:z0037v8z
'''
import urllib2
import proxy

URL_TFS_BOARD = 'https://tfs.audiology-solutions.net/tfs/Prod/Audiology/Mozart%20Team/_backlogs/taskboard/Fitting/Current/Iteration%2055#_a=requirements'
# username = 'z0037v8z'
# password = 'Aa12345!'
# password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
# password_mgr.add_password(None, URL_TFS_BOARD, username, password)

# handler = urllib2.HTTPBasicAuthHandler(password_mgr)
# opener = urllib2.build_opener(handler)
# urllib2.install_opener(opener)
header = {'Authorization':'NTLM TlRMTVNTUAADAAAAGAAYAJYAAAAYABgArgAAABIAEgBYAAAAEAAQAGoAAAAcABwAegAAAAAAAADGAAAABYKIogYBsR0AAAAPYEpIGxr9vOpzFsqNiCUumkEAVQBEAEkATwBMAE8ARwBZAFoAMAAwADMANwBWADgAWgBIAEEAVQBTAEcAUwBHAFAAMgAyADIAMAAwAEMAz//z48hx7egAAAAAAAAAAAAAAAAAAAAAnJv+25WhNPdO0MTFPXur6x1lpj13/skE',
          'Cookie':'__RequestVerificationToken_L3Rmcw2=G9TEn0gTkGaQAWTE_jjmcLatFVkjM36waprX9AjouN-yMPoWlO_SkiquRh6HqVGxND0CnwJXzRnVhn5mwP8dFw5MZCo1; __RequestVerificationToken253ce9edd-2b72-4e40-95c3-4166e104e386=G9TEn0gTkGaQAWTE_jjmcLatFVkjM36waprX9AjouN-yMPoWlO_SkiquRh6HqVGxND0CnwJXzRnVhn5mwP8dFw5MZCo1',
          }

request = urllib2.Request(URL_TFS_BOARD, headers=header)

print urllib2.urlopen(URL_TFS_BOARD).read()
