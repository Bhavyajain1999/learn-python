# Write code here
def most_used(s):

  d = {}
  for i in s.split():
    if i in d:
      d[i] = d[i] + 1
    else:
      d[i] = 1

  max_val = max(d.values())

  for i in d:
    if d[i] == max_val:
      print(i,'->',d[i])
      break

most_used('hello hello hello you i am fine thank you')
