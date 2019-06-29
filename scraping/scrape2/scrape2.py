import os
import shutil
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url0="https://www.youtube.com/"
url1="https://galleria.io/"
url="http://www.chrisburkard.com"
youtube_r=requests.get(url)
yt_soup=BeautifulSoup(youtube_r.text, 'html.parser')
 
# print(yt_soup.findAll('img'))


#use of selenium
driver=webdriver.Firefox()
# driver.get("http://www.youtube.com")
driver.get(url)


iterations=0
while iterations<10:
	html = driver.execute_script(" return document.documentElement.outerHTML")
	#html >will rpint code
	sel_soup=BeautifulSoup(html,'html.parser')
	#get all elements
	print(len(sel_soup.findAll("img")))
	images=[]
	for i in sel_soup.findAll("img"):
		# print(i)
		src=i["src"]
		images.append(src)
	print(images)
	current_path=os.getcwd()
	for img in images:
		try:
			file_name = os.path.basename(img)
			img_r=requests.get(file_name, stream=True)
			new_path=os.path.join(current_path,"images",file_name)
			with open(new_path,"wb") as output_file:
				shutil.copyfileobj(img_r.raw, output_file)
			del img_r
		except:
			pass
	iterations+=1
	time.sleep(5)

# the need to use selenium is that one parse directly the code from server, but some code runs on the frontend [javascript] and is required to run before obtaining everythong else
