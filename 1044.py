a,b = raw_input().split()

a = int(a)
b = int(b)

if a%b == 0 or b%a == 0:
	print'Sao Multipos'
else:
	print 'Nao sao Multiplos'
