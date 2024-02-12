# Define the elements
elements = [1, 2, 3, 4]

# Generate and print all unique permutations
for a in elements:
    for b in elements:
        if b != a:
            for c in elements:
                if c != a and c != b:
                    for d in elements:
                        if d != a and d != b and d != c:
                            print(a, b, c, d)



# # Code here
# for i in range(1,5):
#   for j in range(1,5):
#     for k in range(1,5):
#       for m in range(1,5):
#         print(i,j,k,m)                            
