# Multiply Adjacent elements (both side) and take sum of right and lest side multiplication result.

t = (1, 5, 7, 8, 10)

L = []

L.append(t[0]*t[1])

for i in range(1,len(t)-1):
  L.append(t[i]*t[i-1] + t[i]*t[i+1])

L.append(t[-1]*t[-2])

print(tuple(L))