# Write code here

def lower_upper(s):
  lower_count = 0
  upper_count = 0

  for i in s:
    if i.islower():
      lower_count += 1
    elif i.isupper():
      upper_count += 1
    else:
      pass

  return lower_count,upper_count

s = 'CampusX is an Online Mentorship Program fOr EnginEering studentS.'
x,y = lower_upper(s)
print('No. of Lower case characters:', x)
print('No. of Upper case Characters:', y)