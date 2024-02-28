# Write code here
def perfect_num(num):

  sum = 0

  for i in range(1,num):
    if num % i == 0:
      sum += i

  return sum == num

perfect_num(29)