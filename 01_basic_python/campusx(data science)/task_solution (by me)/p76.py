# Write code here

def bow(L):

  vocab = set()

  for i in L:
    vocab.update(i.split())

  result = []

  for i in L:
    result.append([])
    for j in vocab:
      result[-1].append(i.count(j))

  print(vocab)
  return result


L = [
    'cat mat rat cat',
     'sat bat fat cat rat',
     'pat cat mat rat'
]

bow(L)


