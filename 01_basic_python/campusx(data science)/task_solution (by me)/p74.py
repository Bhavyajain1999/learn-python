# Write code here
import math

def histogram(L):

  min_bin = math.floor(min(L)/10)*10
  max_bin = math.ceil(max(L)/10)*10

  d={}

  for i in range(min_bin,max_bin,10):
    count = 0
    for j in L:
      if i+1<=j<=i+10:
        count+=1

    d[str(i+1) + '-' + str(i+10)] = count

  return d

histogram([13,42,15,37,22,39,41,50])



  



