import requests
from bs4 import BeautifulSoup

url0="https://www.yelp.com/search?find_desc=ensaladas&find_loc=Mexico"
base_url="https://www.yelp.com/search?find_desc={}&find_loc={}"
location="Mexico"#"New York, NY"
lookingfor="ensaladas"
page =0 #paginacion



url=base_url.format(lookingfor,location) + "&start="+str(page)


print(url)


yelp_r=requests.get(url)
#yelp_r #<Response [200]>
# yelp_r.response #200
#yelp_r.text fetch the whole code

yelp_soup=BeautifulSoup(yelp_r.text,'html.parser')
print(yelp_soup.prettify())

#print(yelp_soup.findAll('a')) #bring all <a> tags!
# print(yelp_soup.findAll('li', {'class':'lemon--a__373c0__IEZFH link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5'})) #bring all <a> tags!
#for name in yelp_soup.findAll('a',{'class','somethins'}): print(name)

biz_list= yelp_soup.findAll('div',{'class':'lemon--div__373c0__1mboc u-padding-t3 u-padding-b3 border--top__373c0__19Owr border-color--default__373c0__2oFDT'})


# save to file

file_path='yelp-{location}.txt'.format(location=location)

with open(file_path, "a") as textfile:
	for biz in biz_list:
		title=biz.findAll('a',{'class':'lemon--a__373c0__IEZFH link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5'})[0].text
		print(title)
		phone=biz.findAll('p',{'class','lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7'})[0].text
		print(phone)
		if len(biz.findAll('p',{'class':'lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7'})) >= 1 :
			address=biz.findAll('p',{'class':'lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7'})[1].text
		if len(biz.findAll('p',{'class':'lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7'})) > 2 :
			address+=", "+biz.findAll('p',{'class':'lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7'})[2].text
		print(address)
		print("=============================")
		page_line= "{title}\n{address}\n{phone}\n\n".format(
			title=title,
			address=address,
			phone=phone)
		textfile.write(page_line)

#==================================================
#this attempt will loop through more pages and clean the DOMTags

import requests
from bs4 import BeautifulSoup

url0="https://www.yelp.com/search?find_desc=ensaladas&find_loc=Mexico"
base_url="https://www.yelp.com/search?find_desc={}&find_loc={}"
location="Mexico"#"New York, NY"
lookingfor="ensaladas"
currentpage =0 #paginacion


while currentpage <= 20:
	print(currentpage)
	url=base_url.format(lookingfor,location) + "&start="+str(currentpage)
	yelp_r=requests.get(url)
	yelp_soup=BeautifulSoup(yelp_r.text,'html.parser')
	biz_list= yelp_soup.findAll('div',{'class':'lemon--div__373c0__1mboc u-padding-t3 u-padding-b3 border--top__373c0__19Owr border-color--default__373c0__2oFDT'})
	currentpage+=10
	# save to file
	# file_path='yelp-{location}-2.txt'.format(location=location)
	# with open(file_path, "a") as textfile:
	for biz in biz_list:
		title=biz.findAll('a',{'class':'lemon--a__373c0__IEZFH link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5'})[0].text
		print(title)
		try:
			phone=biz.findAll('p',{'class','lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7'})[0].text
		except:
			print(phone)
		# try:		
		# 	address=biz.findAll('p',{'class':'lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7'})[1].text
		# except:
		# 	address:None 
		# try:
			# address+=", "+biz.findAll('p',{'class':'lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7'})[2].text
		#except:
			#nothing
			#ESTO MERECE ADECUARSE A UN MEJOR CODIGO DOM
		address=biz.findAll('p',{'class':'lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7'})[1].contents
		print(address)
		secondline=""
		first_line=""
		for item in address:
			if "br" in str(item):
				print(item.getText())
				secondline+=item.getText()
			else:
				print(item.strip(" \n\t\r"))
				first_line=item.strip("\n\t\r")
		print(first_line)
		print(secondline)
		#formated address
		print("=============================")
		page_line= "{title}\n{address}\n{phone}\n\n".format(
			title=title,
			address=address,
			phone=phone)
			# textfile.write(page_line)
	


# When using findAll, instead of using .text you can use getText() and extra methods
# such as: findAll().getText().strip('\n\t\r') and is going to remove that


#==================================================



#==================================================

#==================================================
#more stuff

if False:
	for link in yelp_soup.findAll('a'):
		print(link)



url2="https://howlongtobeat.com/"




