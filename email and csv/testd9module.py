from testd9 import MessageUser 

print("123as")
obj= MessageUser()
obj.add_user("Justin",123.12,email="hello@teamcfe.com")
obj.add_user("JoHn",12.13)
obj.add_user("popo",00,email="popo@aguada.com")
obj.add_user("Amy",999.00)
obj.get_details()

print(obj.make_messages())