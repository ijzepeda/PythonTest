from argparse import ArgumentParser

#from data_manager import read_data
from data_class import UserManager
from utils.templates import get_template, render_context


parser = ArgumentParser(prog="hungry")
parser.add_argument("type", type=str, choices=['view', 'message'])
#parser.add_argument("did_send", type=str, choices=['true', 'false'])
parser.add_argument('-id', '--user_id', type=int)
parser.add_argument('-e', '--email', type=str)

args = parser.parse_args()




if args.type == "view":
    print(UserManager().get_user_data(user_id=args.user_id))
    print(UserManager().get_user_data(email=args.email))
elif args.type == "message":
	file_='templates.email_message.txt'
	file_html= 'templates/email_message.html'
	template =  get_templates(file_)
	template_html - get_template(file_html)
	context={
	"name","Justin",
	"date",None,
	"total",None
	}
	print(render_context(template,context))
	print(render_context(template_html,context))
	print("send message")