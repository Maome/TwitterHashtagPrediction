import json
import operator
import re

with open('data.json','rb') as fp:
    wordDict = json.load(fp)
    
newTweet = raw_input("enter tweet:")

newTweet = newTweet.lower()
newTweet = re.sub('[!@#\'$\.,-?\*]', '', newTweet)

newTweet = newTweet.split()
newTweetTemp = newTweet
newTweet = []
[newTweet.append(x) for x in newTweetTemp if x not in newTweet]

#print newTweet
wordsubs = reduce(lambda z, x: z + [y + [x] for y in z], newTweet, [[]])
suggestedTags = {}

for i in wordsubs:
    string = ' '.join(map(str, i))
    #print string
    if string in wordDict:
        for ht in wordDict[string]:
            #print "    " + str(wordDict[string][ht])
            if not ht in suggestedTags:
                suggestedTags[ht] = 0.0
            if suggestedTags[ht] < wordDict[string][ht]:
                suggestedTags[ht] = wordDict[string][ht]

"""
for word in newTweet:
    #print "\n\n" + word
    if word in wordDict.keys():
        for ht in wordDict[word].keys():
            if not ht in suggestedTags.keys():
                suggestedTags[ht] = 0.0
            suggestedTags[ht] += wordDict[word][ht]
            #print ht + ":" + str(wordDict[word][ht])
"""            
#print suggested tags in order
for x in reversed(sorted(suggestedTags.iteritems(), key=operator.itemgetter(1))):
    print "%.2f #" % x[1] + x[0]
