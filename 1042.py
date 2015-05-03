a,b,c = raw_input().split()

a = int(a)
b = int(b)
c = int(c)


if a >= b  and a >= c:
	if b >= c:
		print c,'\n',b,'\n',a
		print '\n',a,'\n',b,'\n',c
	else:
		print b,'\n',c,'\n',a
		print '\n',a,'\n',b,'\n',c
elif b >= a and b >= c:
	if a >= c:
		print c,'\n',a,'\n',b
		print '\n',a,'\n',b,'\n',c
	else:
		print a,'\n',c,'\n',b
		print '\n',a,'\n',b,'\n',c
else:
	if a >= b:
		print b,'\n',a,'\n',c
		print '\n',a,'\n',b,'\n',c
	else:
		print a,'\n',b,'\n',c
		print '\n',a,'\n',b,'\n',c
		

