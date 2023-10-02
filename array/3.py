#Write a Python program to reverse the order of the items in the array.
a=[1,2,3,4]
output=[]
for i in range(len(a)-1,-1,-1):
    output.append(a[i])
print(output)


