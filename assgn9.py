import math
points={
    'p1':(0.1,0.6),
    'p2':(0.15,0.71),
    'p3':(0.08,0.9),
    'p4':(0.16,0.85),
    'p5':(0.2,0.3),
    'p6':(0.25,0.5),
    'p7':(0.24,0.1),
    'p8':(0.3,0.2)
}

def distance(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

m1=points['p1']
m2=points['p8']
c1=[]
c2=[]
print("Old Centroids : ", m1, m2)
for name, p in points.items() :
    d1=distance(m1,p)
    d2=distance(m2,p)
    if d1<d2 :
        c1.append(name)
    else :
        c2.append(name)

def compcent(cl):
    x=[points[p][0] for p in cl]
    y=[points[p][1] for p in cl]
    return (sum(x)/len(x) , sum(y)/len(y))

m1=compcent(c1)
m2=compcent(c2)
print("New Centroids : ", m1, m2)
print("Population of cluster around m2 : ", len(m2))
posp6="c1" if "p6" in c1 else "c2"
print("Cluster of p6 : ", posp6)
print("Cluster 1 : ", c1)
print("Cluster 2 : ", c2)
