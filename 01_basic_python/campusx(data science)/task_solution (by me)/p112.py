# Write code here
l = [{0:2},2,3,4,'5', {5:10}]
# For calculating sum of above list
s=0
for i in range(len(l)):
    try:
        s += l[i]
    except TypeError:
        try:
            s += l[i].get(i)
        except AttributeError:
            s += int(l[i])
print(s)