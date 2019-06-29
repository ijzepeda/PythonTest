import argparse
from data_manager import read_data

parser= argparse.ArgumentParser(prog="hungy")
parser.add_arguments("type",type=str,choices=['view','message'])
parser.add_argument('-id','--user_id',type=int)#-id is the shortcut to --user_id
parser.add_argument('-e','--email',type=str)

args=parser.parse_args()

print(args)
print(args.user_id)



if args.type=="view":
	print(read_data(user_id=args.user_id))
	print(read_data(email=args.email))		
elif args.type=="message":
print("message id")	
