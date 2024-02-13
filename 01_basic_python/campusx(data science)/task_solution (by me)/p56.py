# write your code here
students = []

num = int(input('enter the number of applicants'))

for i in range(num):
  print('Enter details of',i+1,'applicant:')
  name = input('enter name')
  h_ed = input('enter higher education')
  p_skill = input('enter primary skill')
  yog = input('enter year of graduation')

  students.append((name,h_ed,p_skill,yog))

required_skill = input('enter required skill')
required_hed = input('enter required higher education')
required_yog = input('enter required year of graduation')

flag = False
for i in students:
  if i[1] == required_hed and i[2] == required_skill and i[3] < required_yog:
    print(i)
    flag = True

if flag == False:
  print('No such candidates')