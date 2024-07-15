# Move all Zeros to the end of the array
a=[1,2,3,0,8,9,0,0,0,5]
sum=0 
for x in range(len(a)-1):
    if a[x]==0:
        sum+=1
print(sum)
for x in range(sum):
    a.remove(0)
for x in range(sum):
    a.append(0)
print(a)