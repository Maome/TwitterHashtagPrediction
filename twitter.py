import json
import re
import operator
from sets import Set

infile = open('parsed.txt')

class Tweet(object):
    def __init__(self, words, hashtags):
        self.words = words
        self.hashtags = hashtags

tweets = []

for line in infile:
    data = json.loads(line)

    punc=(",./;'?&-")
    line= data['text'].lower()
    words = re.sub('[!@#\'$\.,-?\*]', '', line)
    words = words.split()
    #words = re.findall(r'\w+',line)
    #print b
    #words = line.lower().split()
    # remove hashtags from words list
    for i in range( len( words)):
        if words[i][0] == '#':
            words[i] = ""
    while words.count("") > 0:
        words.remove("")
    
    hashtags = data['entities']['hashtags']
    for i in range( len(hashtags)):
        hashtags[i] = hashtags[i]['text'].lower()
    tweets.append(Tweet(words, hashtags))

print "Twatting tweets..."
hashtagSupport = {}
for twat in tweets:
    #print twat.words
    #print twat.hashtags
    #print

    #get list of hashtags
    #for hashtag in twat.hashtags:
     #   hashtagSet.add(hashtag)
    for ht in twat.hashtags:
        #print ht
        #print hashtagSet[ht]
        if not(ht in hashtagSupport.keys()):
            hashtagSupport[ht] = 0
        hashtagSupport[ht] += 1

print "Removing hashtags with low support..."
#clear hashtags with low support
supportLimit = 20
for ht in hashtagSupport.keys():
    if hashtagSupport[ht] < supportLimit:
        del hashtagSupport[ht]


    #for each ht compute support omg done already lol
print "Reticulating hashtag splines... (this could take a while)"
wordDict = {}
    #cout each tag-word pair
for ht in hashtagSupport.keys():
    for twat in tweets:
        if ht in twat.hashtags:
            for word in twat.words:
                if not (word in wordDict.keys()):
                    wordDict[word] = {}
                if not (ht in wordDict[word].keys()):
                    wordDict[word][ht] = 0
                wordDict[word][ht] += 1

#divide by support for confidence
#remove tags for words below new confidence level
confidenceLimit = 0.2
for word in wordDict.keys():
    for ht in wordDict[word].keys():
        wordDict[word][ht] = float( wordDict[word][ht]) / float(hashtagSupport[ht])
        if (wordDict[word][ht] < confidenceLimit):
            del wordDict[word][ht]
    if wordDict[word] == {}:
        del wordDict[word]



    #save in dictionary by word (wait idk about this one)

#for x in sorted(hashtagSet.iteritems(), key=operator.itemgetter(1)):
#    print x


#for x in sorted(wordDict.iteritems(), key=operator.itemgetter(0)):
#    print x

#Dump dictionary to file
with open('data.json', 'wb') as fp:
    json.dump(wordDict, fp)
