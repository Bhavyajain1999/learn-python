# write your code here
test_list = ["DataScience", 3, 97, "is", 8,91]
key_list = ["name", "id","marks"]

n = len(test_list)
k = len(key_list)
res = []
# list_of_dicts = [{key: value} for key, value in list(zip(key_list, test_list))]
# print(list_of_dicts)
for i in range(0,n,k):
  res.append({key_list[0]: test_list[i],key_list[1]:test_list[i+1],key_list[2]:test_list[i+2] })

print(res)


# values = [1, 2, 3, 4, 5]
# keys = ['a', 'b', 'c', 'd', 'e']

# # Using list comprehension to create list of dictionaries
# list_of_dicts = [{key: value} for key, value in zip(keys, values)]

# print(list_of_dicts)
