# Write code here
def function(l: list, s, **args):
    last_element = l[-1]
    
    l[int(s)]=10
    any_element = l[int(s)+10]
    l[s]=10
    
    res = sum(l)
    
    p = args['p']
    # print(p)
    return res/last_element * p + any_element
try:
    res = function([1,2,1]*9, 12, p=10)
except IndexError as i:
    print(type(i))
    print(i)
except ValueError as v:
    print(type(v))
    print(v)
except TypeError as t:
    print(type(t))
    print(t)
except KeyError as k:
    print(type(k))
    print(k)
except ZeroDivisionError as z:
    print(type(z))
    print(z)
else:
    print("Result:", res)
finally:
    print("Thank you")