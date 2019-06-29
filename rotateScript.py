import time
import curses

# s=curses.initscr()
# curses.curs_set(0)
# sh,sw

counter=0
char1="●"
char2="・"
char3=" "
str_="\t\t\t"
forward=True
limit=5
base=0


while True:
	# sys.stdout.write("\033[F")
	str_="\t"
	for x in range(0,counter-1):
		str_+=char3
		# if(counter==x):
	if forward:
		str_+=char1
		counter+=1
	else:
		str_+=char2
		counter-=1
	if counter==limit and forward:
		forward=False
		print(str_+"\t"+str_+"\t"+str_)
		str_=str_[:-1]+char3+str_[-1:]
	elif counter==base and forward==False:
		forward=True
		# print(str_)
	print(str_+"\t"+str_+"\t"+str_)
	time.sleep(0.1)



# ===

ivan1="Ivan"
ivan2="iVan"
ivan3="ivAn"
ivan4="ivaN"
name=""
	print(namin())
def namin():
	if counter == 0 or counter ==4 or counter ==8:
		name=ivan1
	if counter == 1 or counter ==5 or counter ==9:
		name=ivan2
	if counter == 2 or counter ==6 or counter ==10:
		name=ivan3
	if counter == 3 or counter ==7:
		name=ivan4
	return name





counter=0
while True:
	print("hello:"=str(counter))
	counter+=1
	sys.stdout.write("\033[F")



import sys
import time

a = 0  
for x in range (0,3):  
    a = a + 1  
    b = ("Loading" + "." * a)
    # \r prints a carriage return first, so `b` is printed on top of the previous line.
    sys.stdout.write('\r'+b)
    time.sleep(0.5)
print(a)
#=========
""""
import time

counter=0
char1="●"
char2="・"
char3=" "
str_="\t\t\t"
forward=True
limit=10
base=0

ivan1="Ivan"
ivan2="iVan"
ivan3="ivAn"
ivan4="ivaN"

while True:
	str_="\t\t\t"
	for x in range(0,counter):
		str_+=char3
		# if(counter==x):
	if forward:
		str_+=char1
		counter+=1
	else:
		str_+=char2
		counter-=1
	if counter==limit and forward:
		forward=False
	elif counter==base and forward==False:
		forward=True
	print(str_)
	time.sleep(0.1)

ivan1="Ivan"
ivan2="iVan"
ivan3="ivAn"
ivan4="ivaN"

"""

"""if counter==limit:
		str_.strip("●")
		str_+="8"
		# str_.replace("●","8")
		# str_=str_[:-1]
		# str_+="8"
	if counter==base:
		str_.strip("・")
		str_+="∞"
		# str_.replace("・","∞")
		# str_="∞"+str_
		"""
	

