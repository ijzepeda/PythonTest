import requests
from requests_oauthlib import OAuth1


url ="https://api.yelp.com/v2/search"

consumer_key=""
consumer_secret=""
user_token=""
user_secret=""

Client_ID=""

API_Key=""

def do_search(term="Food",location="Mexico"):
	base_url="https://api.yelp.com/v2/search"
	# term=term.replace(" ","+") #Or URL Encoding
	# location=location.replace(" ","+")
	# url= "{base_url}?term={term}&location={location}".format(
	# 	base_url=base_url,
	# 	term=term,
	# 	location=location
	# 	)
	auth= OAuth1(consumer_secret,consumer_key,
		user_token,user_secret)
	params={
		"term":term,
		"location":location,
	}
	r = request.get(url,auth=auth,params)
	return r.json()


search1= do_search()

for i in search1:
	print(i["name"])
	print(i["phone"])
	print(i["image_url"])
	print(i["location"]["display_address"])
	print(i["location"]["city"])
	print(i.get("name"))
	print(i.get("phone"))
	print(i.get("image_url"))
	print(i.get("location").get("area"))
#Difference between ["value"] vs .get("get") is that gt, will return None in case is null