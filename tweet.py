import json
import operator
import re

with open('data.json','rb') as fp:
    wordDict = json.load(fp)
    
newTweet = raw_input("enter tweet:")

newTweet = newTweet.lower()
newTweet = re.sub('[!@#\'$\.,-?\*]', '', newTweet)

newTweet = newTweet.split()

suggestedTags = {}

for word in newTweet:
    #print "\n\n" + word
    if word in wordDict.keys():
        for ht in wordDict[word].keys():
            if not ht in suggestedTags.keys():
                suggestedTags[ht] = 0.0
            suggestedTags[ht] += wordDict[word][ht]
            #print ht + ":" + str(wordDict[word][ht])
            
#print suggested tags in order
for x in reversed(sorted(suggestedTags.iteritems(), key=operator.itemgetter(1))):
    print x
