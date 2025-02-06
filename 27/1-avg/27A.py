f=f=open("27B.txt")
k1=[]
k2=[]
for s in f:
    x,y=map(float,s.split())
    if y<15: k1.append([x,y])
    else: k2.append([x,y])
def r(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5
def f(k):
    minr=10**10
    for x0,y0 in k:
        sumr=0
        for x,y in k:
            sumr+=r(x0,y0,x,y )
        if sumr<minr:
            minr=sumr
            xc,yc=x0,y0
    return xc,yc
x_k1,y_k1=f(k1)
x_k2,y_k2=f(k2)
print((x_k1 + x_k2)/2 *10000, (y_k1 + y_k2)/2 *10000)


