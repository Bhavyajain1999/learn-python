# # # Combine two lists index-wise(columns wise)
# list1 = ["m","na","i","bha"]
# list2 = ["y","me","s","vya"]


# #mehtod1
# # output = list(zip(list1,list2))

# # print(output)

# #method2

# # # # Write code here
list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]

output = [[i,j] for (i,j) in list(zip(list1,list2))]

print(output)
