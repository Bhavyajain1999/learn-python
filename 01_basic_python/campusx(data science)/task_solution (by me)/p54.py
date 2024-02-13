t1 = (1,2,3,0)
t2 = (1,2,3,0)

flag = True
for i,j in zip(t1,t2):
  if i == j:
    continue
  else:
    flag = False
    break
if flag:
  print('same')
else:
  print('not same')