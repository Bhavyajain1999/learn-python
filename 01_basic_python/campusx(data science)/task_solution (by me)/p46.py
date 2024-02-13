# Code here
# initializing list
test_list = ["campusxIs", "bestFor", "dataScientist"]
 
res = []

for i in test_list:
    temp = [[]]
    for char in i:
        
        if char.isupper():
            temp.append([])
        
        temp[-1].append(char)
    
    temp_string = ""
  
    for item in temp:
        temp_string = temp_string + "".join(item) + " "
    res.append(temp_string[0:-1])

print(res)