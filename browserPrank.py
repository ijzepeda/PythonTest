import webbrowser #open browsers
import time #control time, like sleep
import random #random ranges or numbers

while True:
	randomSite=random.choice(['google.com','yahoo.com','bing.com','reddit.com']) #a list of sites that are going to be selected randomly and used as a value (string) only
	visit = "http://{}".format(randomSite)# change the style of text, and format it to url
	webbrowser.open(visit) #execute webbrowser to open the formatted url
	seconds=random.randrange(5,20) #set a random amount of seconds to open the site, or wait to open the new one
	time.sleep(seconds) # put loop to sleep this amount of time, before opening another website