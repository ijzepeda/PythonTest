import requests


account_sid=""
auth_token=""

test_sid=""
test_auth_token=""

username=account_sid
password=auth_token


number_to_text="+"
twilio_number = "+"

message_body="Hello nerd"

#seems like old method
def xml_pretty(xml_string):
	import xml.dom.minidom
	xml=xml.dom.minidom.parseString(xml_string)
	pretty_xml_ = xml.toprettyxml()
	print(pretty_xml_)

base_url="https://api.twilio.com"
message_url = base_url+ "/2010-04-01/Accounts/" + account_sid + "/Messages"
auth_cred=(username,password)

post_data= {
	"From":twilio_number,
	"To":number_to_text,
	"Body":message_body,
    "MediaUrl":"",

}

r=requests.get(message_url,data=post_data, auth=auth_cred)

print(r.status_code)
xml_pretty(r.text)
