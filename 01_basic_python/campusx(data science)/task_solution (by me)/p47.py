# # Write a program that can perform union operation on 2 lists

# L1 = [1,2,3,4,5,1]
# L2 = [2,3,5,7,8]

# union = []

# for i in L1:
#     if i not in L2 and i not in union:
#         union.append(i)

# for i in L2:
#     if i not in L1 and i not in union:
#         union.append(i)        
  
# for i in L1:
#     if i in  L2 and i not in union:
#         union.append(i)

# for i in L2:
#     if i in L1 and i not in union:
#         union.append(i)          
    

# union.sort()

# print(union)        

# Write code here
L1 = [1,2,3,4,5,1]
L2 = [2,3,5,7,8]

union = []

for i in L1:
  if i not in union:
    union.append(i)

for j in L2:
  if j not in union:
    union.append(j)

print(union)