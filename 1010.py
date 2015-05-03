ent1 = raw_input().split()
ent2 = raw_input().split()

print 'VALOR A PAGAR: R$ ' + '%.2f'%((int(ent1[1])*float(ent1[2])) + (int(ent2[1])*float(ent2[2])))
