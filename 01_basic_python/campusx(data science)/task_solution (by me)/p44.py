L = ['CampusX is a channel', 'for data-science', 'aspirants.']
inp = 'a'
result = []
for i in L:
  result.extend(i.split(inp))

print(result)