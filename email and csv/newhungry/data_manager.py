import csv
import datetime
import shutil
from tempfile import NamedTemporaryFile
import os

"""Posible problems:
how the file is named
where we call the function
"""
file_item_path= os.path.join(os.getcwd(),"data.csv") #not using the current working directory > depende de donde se llame el comando
file_item_path2= os.path.join(os.path.dirname(__file__),"data.csv") #but instead the filepath

def read_data(user_id=None, email=None): #userid is reserved? in python2
    filename = file_item_path2
    print(filename)
    with open(filename,"r") as csvfile:
        reader = csv.DictReader(csvfile)
        items = []
        unknown_user_id = None
        unknown_email = None
        for row in reader:
            if user_id is not None:
                if user_id== row.get("id"):#if int(user_id) == int(row.get("id")):
                    return row
                else:
                    unknown_user_id = user_id
            if email is not None: #in case default parameter, is not none
                if email == row.get("email"):
                    return row
                else:
                    unknown_email = email
        if unknown_user_id is not None:
            return "User id {user_id} not found".format(user_id=user_id)
        if unknown_email is not None:
            return "Email {email} not found".format(email=email)
    return None
