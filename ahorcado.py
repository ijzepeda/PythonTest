#ahorcado

import time
# import window

nombre=input("Como te llamas? ")
# window.clear
print ("Bienvenido al ahorcado " + nombre)
print (" ")
time.sleep(1)
print ("comienza a adivinar")
time.sleep(0.5)
palabra="ijzepeda es chidoliro"
tupalabra=""
vidas=5

while vidas > 0:
	fallas=0
	for letra in palabra:      #cada letra de la palbra, una por una, y se va checando y comparando
		if letra in tupalabra:
			print(letra,end="")#end="" > 
		else:
			print("*",end="")#para que la proxima end no salte deliena?
			fallas+=1
	if fallas == 0:
		print("\nFelicidades, ganaste!")
		break

	print("")
	tuletra=input("Introduce una letra: ")
	tupalabra+=tuletra

	if tuletra not in palabra:
		vidas-=1		
		print("\nTe equivocaste. ")
		print("Ahora tienes ",+vidas," vidas. usando  \",+\" para concatenar!") #el uso de comas ayudo a concatenar un int en un string!!
		print("Ahora tienes "+str(vidas)+" vidas.<Metodo de string! ") #el uso de comas ayudo a concatenar un int en un string!!
	if vidas<=0:
		print("Perdiste! ")
else:
	print("Gracias por participar. ")






