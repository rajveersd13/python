#Largest Element in an Array
a=[1,2,3,4,5,6,7,8,9,10]
max=a[0]
for i in range(len(a)):
    if (max<a[i]):
        max=a[i]
print(max)

