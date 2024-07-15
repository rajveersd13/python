#Linear Search
a=[1,2,3,4,5,6,7,8]
num=8
print(len(a))
for x in range(len(a)-1):
    if a[x]==num:
        print(x)
        break
