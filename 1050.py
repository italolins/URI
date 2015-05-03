ddd = [11,19,21,27,31,32,61,71]
cid = ['Sao Paulo','Campinas','Rio de Janeiro','Vitoria',
		'Belo Horizonte','Juiz de Fora','Brasilia','Salvador']
		
a = int(raw_input())

if a in ddd:
	for i in xrange(8):
		if a == ddd[i]:
			print cid[i]
			break
else:
	print 'DDD nao cadastrado'
