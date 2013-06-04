import json

infile = open('parsed.txt')

class Tweet(object):
    def __init__(self, words, hashtags):
        self.words = words
        self.hashtags = hashtags

tweets = []

for line in infile:
    data = json.loads(line)
    
    words = data['text'].split()
    # remove hashtags from words list
    for i in range( len( words)):
        if words[i][0] == '#':
            words[i] = ""
    while words.count("") > 0:
        words.remove("")
    
    hashtags = data['entities']['hashtags']
    for i in range( len(hashtags)):
        hashtags[i] = hashtags[i]['text']
    tweets.append(Tweet(words, hashtags))

for twat in tweets:
    print twat.words
    print twat.hashtags
    print
