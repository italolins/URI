for i in xrange(int(raw_input())):
	a,b = raw_input().split()
	a = int(a)
	b = int(b)
	soma = 0
	if( a >= b ):
		for i in xrange(b+1,a):
			if(i%2 == 1):
				soma += i
	else:
		for i in xrange(a+1,b):
			if(i%2 == 1):
				soma += i
	print soma
