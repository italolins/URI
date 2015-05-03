a = float(raw_input())

if a <= 800:
	if a <= 400:
		print 'Novo salario:','%.2f'%(a+a*0.15),'\nReajuste ganho:','%.2f'%(a*0.15),'\nEm precentual: 15 %'
	else:
		print 'Novo salario:','%.2f'%(a+a*0.12),'\nReajuste ganho:','%.2f'%(a*0.12),'\nEm precentual: 12 %'
elif a <= 2000:
	if a <= 1200:
		print 'Novo salario:','%.2f'%(a+a*0.1),'\nReajuste ganho:','%.2f'%(a*0.1),'\nEm precentual: 10 %'
	else:
		print 'Novo salario:','%.2f'%(a+a*0.07),'\nReajuste ganho:','%.2f'%(a*0.07),'\nEm precentual: 7 %'
else:
	print 'Novo salario:','%.2f'%(a+a*0.04),'\nReajuste ganho:','%.2f'%(a*0.04),'\nEm precentual: 4 %'
