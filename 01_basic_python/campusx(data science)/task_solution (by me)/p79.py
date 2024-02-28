# Write code here
str1="FIFA world cup in 2022 will take place in Qatar"

list(filter(lambda x:True if x.lower() in 'aeiou' else False,str1))