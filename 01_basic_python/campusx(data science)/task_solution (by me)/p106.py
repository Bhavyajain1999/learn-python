string  = 'DataScience'

def string_length(s):
    if s == "":
        return 0
    else:
        return 1 + string_length(s[1:])
string_length(string)