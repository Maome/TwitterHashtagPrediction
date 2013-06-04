import json

myfile = file("datatweets")
outfile = open('parsed.txt', 'r+')

for line in myfile:
    data = json.loads(line)
    if data['text'][0:2] != "RT" and data['text'][0:1] != '@' and data['entities']['hashtags'] != []:
        print data['text']#, "#%s" % data['entities']['hashtags'][0]['text']
        outfile.write(line)

outfile.close()
