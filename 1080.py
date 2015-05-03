maior = int(raw_input())
indice = 1;
for i in xrange(1,100):
	ent = int(raw_input())
	if(ent > maior):
		maior = ent
		indice = i+1
		
print maior
print indice
