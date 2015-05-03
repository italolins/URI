ent = raw_input().split()

media = (float(ent[0])*2 + float(ent[1])*3 + float(ent[2])*4 + float(ent[3]))/10.

if(media >= 7.):
	print 'Media :','%.1f'%media, '\n' + 'Aluno aprovado.'
elif(media >= 5.):
	print 'Aluno em exame.'
	aux = float(raw_input())
	final = (media+aux)/2.
	if final >= 5.:
		print 'Nota Exame:',aux,'\n' + 'Aluno aprovado.' + '\n' + 'Media final:','%.1f'%final
	else:
		print 'Nota Exame:',aux,'\n' + 'Aluno reprovado.' + '\n' + 'Media final:','%.1f'%final
else:
	print 'Media :','%.1f'%media, '\n' + 'Aluno reprovado.'
