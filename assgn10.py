import math

points={
    "p1":(2,10),
    "p2":(2,5),
    "p3":(8,4),
    "p4":(5,8),
    "p5":(7,5),
    "p6":(6,4),
    "p7":(1,2),
    "p8":(4,9)
}

m1=points['p1']
m2=points['p4']
m3=points['p7']
print("Old Centroids : ",m1, m2, m3)

def distance(x, y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

c1=[]
c2=[]
c3=[]

for name, p in points.items():
    d1=distance(m1, p)
    d2=distance(m2, p)
    d3=distance(m3, p)
    dis=[d1, d2, d3]
    if min(dis)==dis[0]:
        c1.append(name)
    elif min(dis)==dis[1]:
        c2.append(name)
    else:
        c3.append(name)


def calcent(cl):
    x=[points[p][0] for p in cl]
    y=[points[p][1] for p in cl]
    return (sum(x)/len(x), sum(y)/ len(y))

m1=calcent(c1)
m2=calcent(c2)
m3=calcent(c3)
print("New Centroids : ", m1, m2, m3)
print("Population of cluster around m3 : ", len(m3))
posp6="c1" if "p6" in c1 else "c2"
print("Cluster of p6 : ", posp6)
print("Cluster 1 : ", c1)
print("Cluster 2 : ", c2)
print("Cluster 3 : ", c3)