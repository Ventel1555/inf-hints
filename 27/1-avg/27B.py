f=open("27A.txt")
k1=[]
k2=[]
k3=[]
for s in f:
    x,y=map(float,s.split())
    if 5.5<y<8.5: k1.append([x,y])
    if 2<y<5: k2.append([x,y])
    if y<0: k3.append([x,y])
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
x_k3,y_k3=f(k3)
print((x_k1 + x_k2+ x_k3)/3 *10000, (y_k1 + y_k2 + y_k3)/3 *10000)

