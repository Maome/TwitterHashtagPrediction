import json

#https://stream.twitter.com/1.1/statuses/sample.json?language=en

myfile = file("datatweets")
outfile = open('parsed.txt', 'r+')

count = 0;

for line in myfile:
    count += 1
    print "Parsing line " + str(count) + "                  \r",
    data = json.loads(line)
    if not "delete" in data.keys():
        if data['user']['lang'] == "en":
            if data['text'][0:2] != "RT" and data['text'][0:1] != '@' and data['entities']['hashtags'] != []:
                #print data['text']#, "#%s" % data['entities']['hashtags'][0]['text']
                outfile.write(line)

outfile.close()
