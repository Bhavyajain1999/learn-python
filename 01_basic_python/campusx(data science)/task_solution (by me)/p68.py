# Write code here

def sort_sequence(seq):
  temp = []

  for i in sorted(seq.split('-')):
    temp.append(i)

  return "-".join(temp)

s = 'green-red-yellow-black-white'
sort_sequence(s)