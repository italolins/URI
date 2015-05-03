ent1 = int(raw_input())
ent2 = int(raw_input())
soma = 0

if ent1 >= ent2:
	for i in xrange(ent2+1,ent1):
		if(i%2 == 1):
			soma += i
else:
	for i in xrange(ent1+1,ent2):
		if(i%2 == 1):
			soma += i
print soma
