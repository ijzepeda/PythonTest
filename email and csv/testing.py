import datetime

today=datetime.date.today()

list=[23,43,23.23,"dgf",432]

def my_sum(listilla):
	total=0
	for x in listilla:
		if isinstance(x,int) or isinstance(x,float):
			total+=x
		#elif isinstance(x,str)
		#	total=total
	return total

def numberizeList(listilla):
	listona=[]
	for element in listilla:
		if isinstance(element, int) or isinstance(element, float):
			listona.append(element)
	return listona

print("sum function")
print(sum(numberizeList(list)))
print("my sum_function")
print(my_sum(list))
print("******************************")

names=["justin", "ivan","Paco","Luis","steve"]
amounts=[199.99,0.0,20.50,100,0]

gen_msg="""Hello {name} 
Thank you f ot your purchase on {date}. \nA reminder, the total was {price}. 
\nThanks\nKC\n\n-----------\n"""

def make_message(names, amounts):
	messages=[]
	if len(names)==len(amounts):
		i=0
		for name in names:
			new_amnt="%.2f" %(amounts[i])
			new_msg= gen_msg.format(name=name[0].upper()+name[1:],
				date='{today.day}/{today.month}/{today.year}'.format(today=today) ,
				price=new_amnt
				)
			i+=1
			print(new_msg)

make_message(names,amounts)


class Animal():
	name="Ani"
	kind="animale"
	noise="grunt"
	color="brown"
	hair="fur"
	action="run"
	def get_color(self):
		return self.color
	def make_noise(self):
		return self.noise
	def get_action(self):
		return self.action
	def description(self):
		return "The "+self.color+" "+self.kind+" "+self.name+", "+self.noise+" to communicate"+". It has "+self.hair+ " and tends to "+self.action

class Dog(Animal):
	kind="dog"
	noise="barks"
	action = "chase"

class Cat(Animal):
	kind="cat"
	noise="meows"
	action="annoy"
	def get_action(self):
		return self.name+ ", the cat enjoys to "+ self.action+ " everytime it cans"


dogo=Dog()
cato=Cat()
dogo.name="Firulais"
cato.name="Terror"
print(dogo.description())
print(cato.description())
print(cato.get_action())







