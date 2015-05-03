a = int(raw_input())
aux = a
notas = [1,2,5,10,20,50,100]
quant = [0,0,0, 0, 0, 0,0]

for i in xrange(7):
	 quant[6 - i] = aux/notas[6-i] 
	 aux = aux%notas[6-i]

print a
for	i in xrange(7):	
	print quant[6 -i],'nota(s) de R$ '+ str(notas[6-i]) + ',00'
