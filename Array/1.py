#Write a Python program to create an array of n integers and display the array items. 
print("Enter the number of elements in array")
n=int(input())
array=[]
for x in range(n):
    print("enter the element  for array")
    s=int(input())
    array.append(s)
print("Array is ", array)
