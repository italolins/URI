a = int(raw_input())
cont = 0
 
if  a%2 == 0:
	a += 1

while True:
	if cont == 6: break
	print a
	a += 2
	cont += 1
