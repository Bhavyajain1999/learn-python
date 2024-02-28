# Write code here

def shortest_dist(points,query):
  temp = []
  for i in points:
    distance = ((i[0] - query[0])**2 + (i[1] - query[1])**2)**0.5
    temp.append(distance)

  return points[sorted(list(enumerate(temp)),key=lambda x:x[1])[0][0]]


points = [(1,4),(2,-2),(13,3),(14,4)]
query = (0,0)

shortest_dist(points,query)