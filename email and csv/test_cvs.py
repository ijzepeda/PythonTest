import csv
import shutil
from tempfile import NamedTemporaryFile

with open("data1.csv", "a") as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["append row","some desc","another"])
	writer.writerow(["row1","col2","c3"])

with open("data1.csv", "r") as csvfile:
	reader= csv.DictReader(csvfile)
	for row in reader:
		print(row)


		#template stuff there is OS
	#

def get_length(file_path):
	with open("data2.csv","r") as csvfile:
		reader = csv.reader(csvfile)
		reader_list=list(reader)	 #crea una lista conforme a los rows del archivo, esta hecho automatico
		print(reader_list)			 
	return len(reader_list)		 #contiene el numero de elementos de reader_list



def append_data(file_path, name, email):
	fieldnames=['id', 'name', 'email']
	#the number of rows?
	next_id= get_length(file_path) #will return the total of rows. else, next use will have an increment
	with open(file_path, "a") as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writerow({
			"id":next_id,
			"name":name,
			"email":email
			})


# append_data("data2.csv","Justin","hello@teamcfe.com")

#edit a file
#i only copy data , edit it , and replace original file

filename="data2.csv"
temp_file=NamedTemporaryFile(delete=False)

with open(filename, "rb") as csvfile, temp_file:
	reader= csv.DictReader(csvfile)
	fieldnames= ['id','name','email','amount','sent']
	writer= csv.DictWriter(temp_file, fieldnames=fieldnames)
	writer.writeheader() 

	for row in reader:
		writer.writerow({
			"id":row["id"],
			"name":row["name"],
			"email":row["email"],
			"amount":"123123",
			"sent":"",
			})
#not working

#BUT
# to replace



def edit_data(edit_id=None, email=None, amount=None, sent=None):
	filename="data.csv"
	temp_file-NamedTemporaryFile(detele=False)

	with open(filename,"rb") as csvfile,temp_file:
		reader=csv.DictReader(csvfile)
		fieldnames=['id','name','email','amount','sent','date']
		fieldnames=csv.DictWriter(temp_file,fieldnames=fieldnames)
		writer.writeheader()
		for row in reader:
			if edit_id is not None:
				if int(row["id"])== int(edit_id)
				row['amount']=amount
				row["sent"]=sent
			elif email is not None and edit_id is None:
				if str(row["email"])==str(email):
					row["amount"]=amount
					row["sent"]=sent
			else:
				pass
			writer.writerow(row)

		shutil.move(temp_file.name,filename)
		return True
	return False

edit_data(email="hello@teamcfe.com", amount=99.99, sent="")


