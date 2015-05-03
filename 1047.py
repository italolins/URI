hi,mi,hf,mf = raw_input().split()

hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)

if hi*60 + mi < hf*60 + mf:
	print 'O JOGO DUROU',hf - hi,'HORA(S) E',
elif hi*60 + mi> hf*60 + mf:
	print 'O JOGO DUROU',(24 - hi) + hf,'HORA(S) E',
else:
	print 'O JOGO DUROU', 24,'HORA(S) E',
