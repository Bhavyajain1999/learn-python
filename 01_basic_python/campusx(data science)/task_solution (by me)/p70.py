# Write code here

def is_even(L):
  res = []

  for i in L:
    if i % 2 == 0:
      res.append(i)

  return res

is_even([1,2,3,4,5,6,7])