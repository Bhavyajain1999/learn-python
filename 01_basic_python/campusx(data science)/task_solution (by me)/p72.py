# Write code here

def merge_dict(*kwargs):
  d = {}

  for i in kwargs:
    d.update(i)

  return d


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

merge_dict(dic1,dic2,dic3)
