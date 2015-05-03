preco = [4.00,4.50,5.00,2.00,1.50]
ent = raw_input().split()

print 'Total: R$','%.2f'%(preco[int(ent[0])-1]*int(ent[1]))
