#Left rotate an array by D places
a=[1,2,3,4,5]
c=int(input())
for x in range(c):
    b=a[0]
    for x in range(len(a)-1):
        a[x]=a[x+1]
    a[len(a)-1]=b
print(a)