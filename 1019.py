entr = int(raw_input())
h = (entr/60)/60
m = (entr/60) - h*60
s = entr - h*60*60 - m*60

print str(h)+":" + str(m) + ":" +str(s)
