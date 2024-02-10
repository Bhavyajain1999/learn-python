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
