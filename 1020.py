ent = int(raw_input())

a = ent/365
m = ent/30 - a*12
d = ent - m*30 - a*365

print a,'ano(s)' + '\n',m,'mes(es)' + '\n',d,'dias(s)'
