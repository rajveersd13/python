#Remove duplicates from Sorted array
a=[1,1,2,3,4,5,6,7,7]
# b=set(a)
# print(b)
c=[]
d=len(a)
for x in range(d-1):
    if a[x]!=a[x+1]:
        c.append(a[x])
if c[-1]!=a[-1]:
    c.append(a[d-1])
print(c)




# You can create a set using curly braces {} or the set() function. 
#Sets are useful when you need to store distinct elements and perform operations like union, intersection, and difference
# Adding Elements WE can add a single element using the add() method.
# You can remove an element using the remove() or discard() method. 
# The difference is that remove() will raise a KeyError if the element is not found, whereas discard() will not.
# The union of two sets is a set containing all elements from both sets.
# The intersection of two sets is a set containing only the elements that are in both sets.
# The difference of two sets is a set containing elements that are in the first set but not in the second.