# Write code here
string = "aabbbcdabcddffgah"

def runEncode(s):
    if len(s) == 0:
        return []
    else:
        index = 1
        while index < len(s) and s[index] == s[index-1]:
            index += 1
        compressed = [s[0], index]
        
        return compressed + runEncode(s[index:])
        
print(runEncode(string))