list=[12,2,3,42]
print(list) #OUTPUT --> [12, 2, 3, 42]
print(type(list)) #OUTPUT -->  # <class 'list'>

#Acessing element
#first element index at zero 
print(list[0]) #OUTPUT -->1

#looping 
for x in list:
    print(x)

#len function
print(len(list)) ##OUTPUT=1

#sorting 
list.sort()
print(list) #OUTPUT --> [2,3,12,42]
 
a = [3, 1, 2]
sorted_a = sorted(a)  # Create a new sorted list and assign it to sorted_a
print(sorted_a)       # This will print the sorted list: [1, 2, 3]
print(a)              # This will print the original unsorted list: [3, 1, 2]
