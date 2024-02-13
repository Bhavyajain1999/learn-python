L = ['1ac21', '23fg', '456', '098d','1','kls']

prodvalue =[]

for i in L:
    product = 1
    for char in i:
        if char.isdigit():
            product = product*int(char)
    prodvalue.append(product)


result = ([i[1] for i in sorted(list(zip(prodvalue,L)),reverse=True)])
print(type(result))