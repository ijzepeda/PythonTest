import email
import imaplib #imap 
from bs4 import BeautifulSoup
import os
import mimetypes

username ="ijzepeda.is.testing.youknow@gmail.com"
password="password"

# https://www.google.com/settings/security/lesssecureapps
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username,password)
mail.select("inbox")
# mail.create("Item2")
# mail.list()
result, data = mail.uid('search', None, "ALL")
#data. > will return an array with numbers each for an email
data[0] #fuera del array
inbox_item_list=data[0].split()
inbox_item_list #print each index for email
for item in inbox_item_list:
	# most_recent=inbox_item_list[-1] #remember that in python , in an array, -1 represents the last one. not a negative or inexistant
	# oldest=inbox_item_list[0]
	#
	result, email_data= mail.uid('fetch', oldest, '(RFC822)')
	raw_email=email_data[0][1].decode("utf-8")
	email_message= email.message_from_string(raw_email)
	#
	# print(dir(email_message))
	to_=email_message["To"]
	from_=email_message["From"]
	subject_=email_message["Subject"]
	date_=email_message["date"]
	#payload is the message in a list
	#iterate the list to retrieve each message
	counter=0
	for part in email_message.walk():
		if part.get_content_maintype() == "multipart":
			continue
		filename= part.get_filename()
		content_type= part.get_content_type()
		if not filename:
			# ext='.html'
			ext= mimetypes.guess_extension(content_type)
			if not ext:
				ext=".bin"
			# if 'text' in content_type:
			# 	ext=".txt"
			# elif "html" in content_type:
			# 	ext=".html"
			filename='msg-part-%08d%s' %(counter, ext)
		counter+=1
	# save file
	save_path=os.path.join(os.getcwd(), "emails", date_, subject_)
	if not os.path.exists(save_path): #if the path doesnt exists
		os.makedirs(save_path)
	with open(os.path.join(save_path,filename),"wb") as fp:
		fp.write(part.get_payload(decode=True))
	# print(subject_)
	# print(content_type)


"""
	if "plain" in content_type:
		print(part.get_payload())
	elif "html" in content_type:
		html_=part.get_payload()
		soup=BeautifulSoup(html_,"html.parser")
		text=soup.get_text()
		print("do some beautiful soup to:"+text)
	else:
		print(content_type)"""
	# email_message.get_payload()



