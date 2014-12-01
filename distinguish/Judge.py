'''

@author: zz
'''

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def isSimilar(word1, word2):
    pass


def charSet(word):
    result = {}
    for c in word:
        if result.has_key(c):
            result[c] += 1
        else:
            result[c] = 1
    return result

def commonChars(charSets):
    result = 0
    for c in ALPHABET:
        allHave = True
        for charSet in charSets:
            if(not charSet.has_key(c)):
                allHave = False
        if allHave:
            result += 1
    return result

print(commonChars([charSet("surly"), charSet("sully"), charSet("sullen")]))