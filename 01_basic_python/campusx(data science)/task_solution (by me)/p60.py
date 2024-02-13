# write your code here
L = [[1, 2, 2, 4, 3, 6],
 [5, 1, 3, 4],
 [9, 5, 7, 1],
 [2, 4, 1, 3]]

s = set()

for i in L:
  s.update(i)

print(s)