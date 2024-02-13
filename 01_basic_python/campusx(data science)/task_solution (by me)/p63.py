# write your code here
test_str = 'CampusX best for DS students.'
repl_dict = {"best" : "is the best channel", "DS" : "Data-Science"}

res = []
for i in test_str.split():
  if i in repl_dict:
    res.append(repl_dict[i])
  else:
    res.append(i)

print(" ".join(res))