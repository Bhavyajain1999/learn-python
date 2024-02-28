# Write code here
def return_unique(L):
  res = []

  for i in L:
    if i not in res:
      res.append(i)

  return res

L = [1,2,3,3,3,3,4,5]
return_unique(L)