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

print "Loading pass..."

lineCount = 0
for line in infile:
    lineCount += 1
    print "\r",
    print "loading line " + str(lineCount) + "                     ",
    
    data = json.loads(line)

    punc=(",./;'?&-")
    line= data['text'].lower()
    words = re.sub('[!@#\'$\.,-?\*]', '', line)
    words = words.split()
    wordsTemp = words
    words = []
    
    removeThese = ['with', 'of', 'off', 'on', 'onto', 'over', 'than', 'through', 'except', 'by', 'via', 'to', 'up', 'down', 'under', 'upon', 'versus', 'at', 'as', 'anti', 'among', 'before', 'after', 'beyond', 'by', 'following', 'for', 'from', 'for' , 'and', 'nor', 'but', 'or', 'is', 'yet', 'so', 'when', 'why', 'that', 'how', 'who', 'where', 'unless', 'because', 'otherwise', 'however', 'therefore', 'thus', 'besides', 'also', 'since', 'until', 'as', 'if', 'while', 'before', 'after', 'although', 'all', 'anybody', 'another', 'any', 'anyone', 'anything', 'both', 'each', 'either', 'everybody', 'everyone', 'few', 'he', 'her', 'him', 'hers', 'herself', 'himself', 'his', 'i', 'its', 'itself', 'me', 'mine', 'my', 'myself', 'none', 'neither', 'nobody', 'one', 'other', 'others', 'our', 'ours', 'she', 'some', 'somebody', 'someone', 'something', 'that', 'their', 'theirs', 'them', 'themselves', 'these', 'they', 'this', 'those', 'us', 'we', 'what', 'whatever', 'which', 'whichever', 'who', 'whoever', 'whom', 'whose', 'you', 'your', 'yours', 'yourself', 'yourselves', 'a', 'about', 'above', 'above', 'across', 'after', 'afterwards', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also','although','always','am','among', 'amongst', 'amoungst', 'amount',  'an', 'and', 'another', 'any','anyhow','anyone','anything','anyway', 'anywhere', 'are', 'around', 'as',  'at', 'back','be','became', 'because','become','becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'bill', 'both', 'bottom','but', 'by', 'call', 'can', 'cannot', 'cant', 'co', 'con', 'could', 'couldnt', 'cry', 'de', 'describe', 'detail', 'do', 'done', 'down', 'due', 'during', 'each', 'eg', 'eight', 'either', 'eleven','else', 'elsewhere', 'empty', 'enough', 'etc', 'even', 'ever', 'every', 'everyone', 'everything', 'everywhere', 'except', 'few', 'fifteen', 'fify', 'fill', 'find', 'fire', 'first', 'five', 'for', 'former', 'formerly', 'forty', 'found', 'four', 'from', 'front', 'full', 'further', 'get', 'give', 'go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'however', 'hundred', 'ie', 'if', 'in', 'inc', 'indeed', 'interest', 'into', 'is', 'it', 'its', 'itself', 'keep', 'last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made', 'many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine', 'more', 'moreover', 'most', 'mostly', 'move', 'much', 'must', 'my', 'myself', 'name', 'namely', 'neither', 'never', 'nevertheless', 'next', 'nine', 'no', 'nobody', 'none', 'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'on', 'once', 'one', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'over', 'own','part', 'per', 'perhaps', 'please', 'put', 'rather', 're', 'same', 'see', 'seem', 'seemed', 'seeming', 'seems', 'serious', 'several', 'she', 'should', 'show', 'side', 'since', 'sincere', 'six', 'sixty', 'so', 'some', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere', 'still', 'such', 'system', 'take', 'ten', 'than', 'that', 'the', 'their', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'these', 'they', 'thickv', 'thin', 'third', 'this', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'top', 'toward', 'towards', 'twelve', 'twenty', 'two', 'un', 'under', 'until', 'up', 'upon', 'us', 'very', 'via', 'was', 'we', 'well', 'were', 'what', 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with', 'within', 'without', 'would', 'yet', 'you', 'your', 'yours', 'yourself', 'yourselves', 'the']
    [words.append(x) for x in wordsTemp if (x not in words and x not in removeThese)]
    
    #print words
    
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

print ""
print "Generating hashtag dictionary..."
hashtagSupport = {}
counter = 0;
for twat in tweets:
    counter += 1
    print "\r",
    print "Tweet #" + str(counter),
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

print ""
print "Removing hashtags with low support..."
#clear hashtags with low support
supportLimit = 20
counter = 0;
for ht in hashtagSupport.keys():
    counter += 1
    print "\r",
    print "Hashtag #" + str(counter),
    if hashtagSupport[ht] < supportLimit:
        del hashtagSupport[ht]


    #for each ht compute support omg done already lol
    
print ""
print "Improved reiculation algorithm... (this could still take a while)"
wordDict = {}

counter = 0;
for twat in tweets:
    counter += 1
    print "\r",
    print "Tweet #" + str(counter),
    for ht in twat.hashtags:
        if ht in hashtagSupport.keys():
            for word in twat.words:
                if not (word in wordDict.keys()):
                    wordDict[word] = {}
                if not (ht in wordDict[word].keys()):
                    wordDict[word][ht] = 0
                wordDict[word][ht] += 1
    
#print ""
#print "Reticulating hashtag splines... (this could take a while)"
#wordDict = {}
#    #cout each tag-word pair
#passcounter = 0
#for ht in hashtagSupport.keys():
#    passcounter += 1
#    counter = 0
#    for twat in tweets:
#        counter += 1
#        print "Pass " + str(passcounter) + "/" + str(len(hashtagSupport)) + " tweet " + str(counter) + "                             \r",
#        if ht in twat.hashtags:
#            for word in twat.words:
#                if not (word in wordDict.keys()):
#                    wordDict[word] = {}
#                if not (ht in wordDict[word].keys()):
#                    wordDict[word][ht] = 0
#                wordDict[word][ht] += 1

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
