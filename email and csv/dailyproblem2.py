"""Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array
 is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
 [120, 60, 40, 30, 24]. If our input was [3, 2, 1],
  the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?"""

list=[1,2,3,4,5]
newlist=[]
totalproduct=1

for x in list:
	totalproduct*=x
	print(totalproduct)


print("total: "+str(totalproduct))


for y in list:
	newlist.append(totalproduct//y)
	print(newlist)
print(newlist)


print("attempt using nested loops")
secondlist=[]
for x in list:
	tempvalue=1
	for y in list:
		if x != y:
			tempvalue*=y
	secondlist.append(tempvalue)
	print(secondlist)

print("------")
print(secondlist)





