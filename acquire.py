import os
import urllib2
import threading
import signal
import sys

exit = False


#signal handler provides clean exit on interrupt (no half tweets as last line)
def signal_handler(signal, frame):
    global exit
    exit = True

signal.signal(signal.SIGINT, signal_handler)

speed = 0.0
counter = 0
newcounter = 0



def timerControl():
    global newcounter
    global speed
    global t
    global exit
    speed = newcounter/2.0
    newcounter = 0
    if exit:
        return
    threading.Timer(2.0, lambda: timerControl()).start()

tweetfile = open('rawtweet', 'a')

url = "https://stream.twitter.com/1.1/statuses/sample.json"

authenticationHandler = urllib2.HTTPPasswordMgrWithDefaultRealm()
authenticationHandler.add_password(None, url, "reillyjonemily" , "twatters")
urllib2.install_opener(urllib2.build_opener(urllib2.HTTPBasicAuthHandler(authenticationHandler)))
req = urllib2.Request(url)


timerControl()

for line in urllib2.urlopen(req):
    counter += 1
    newcounter += 1
    os.system('clear')
    print "Acquired " + str(counter) + " tweets..."
    print str(speed) + " tweets per second"
    tweetfile.write(line)
    if exit:
        break
