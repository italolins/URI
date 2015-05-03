cont = 0
soma = 0
for i in xrange(6):
	a = float(raw_input())
	if a > 0:
		cont += 1
		soma += a
		
print cont,'valores positivos' + '\n','%.1f'%(soma/cont)

