import difflib

#print(difflib.SequenceMatcher(None, '', 'surly').ratio())

file = open("1.txt", encoding="utf-8")
content = file.read()
groups = content.split('\n\n')
for group in groups:
	if(group.count('\n') > 0):
		words = group.split('\n')
		n = len(words)
		for i in 0,n-2:
			print(words[i] + " and " + words[i+1] + ":" + str(difflib.SequenceMatcher(None, words[i], words[i+1]).ratio()))
			print(words[i] + " and " + words[i+1] + ":" + str(difflib.SequenceMatcher(None, words[i+1], words[i]).ratio()))
			
print("#END")