ent = float(raw_input())

if(ent > 100 or ent < 0):
	print 'Fora de intervalo'
else:
	if(ent <= 50):
		if(ent <= 25):
			print 'Intervalo [0,25]'
		else:
			print 'Intervalo (25,50]'
	else: 
		if(ent <= 75):
			print 'Intervalo (50,75]'
		else:
			print 'Intervalo (75,100]'
