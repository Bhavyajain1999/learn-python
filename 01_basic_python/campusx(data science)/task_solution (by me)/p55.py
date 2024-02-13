# Count no of tuples, list and set from a list

# write your code here
L = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]
output = [0,0,0]

for i in L:
  if type(i) == list:
    output[0] = output[0] + 1
  elif type(i) == set:
    output[1] = output[1] + 1
  elif type(i) == tuple:
    output[2] = output[2] + 1
  else:
    pass

print('Lists-{}\nSets-{}\nTuples-{}'.format(output[0],output[1],output[2]))

