par = 0
pos = 0
sub = 0
for i in xrange(5):
	a = int(raw_input())
	if (a)%2 == 0:
		par += 1
	if a >= 0:
		pos += 1
	if a == 0:
		sub += 1

print par,'valor(es) par(es)'
print 5 - par,'valor(es) impar(es)'
print pos - sub,'valor(es) positivo(s)'
print 5-pos,'valor(es) negativo(s)'
