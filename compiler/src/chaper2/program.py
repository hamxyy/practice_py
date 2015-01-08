'''
Created on 5 Jan, 2015

@author: z0037v8z
'''
from chaper2.simpletranslater import parse

file = open('sample.z', 'r')
postfix = parse(file.read())
print(postfix)