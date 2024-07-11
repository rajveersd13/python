#string 

#1.
string="happy Diwali" #always string in written in Quotation
print(string)  #OUTPUT -->happy Diwali

#2.Multiline string
a='''1st line
2nd line
3rd line'''
print(a) # OUTPUT ---> 1st line
#                       2nd line
#                       3rd line
 
#3.Strings are Arrays of bytes representing unicode characters.
print(string[0:5])

#FUNCTIONS
#1. STRING LENGTH
print(len(string))
#2. upper
print(string.upper()) #output--> HAPPY DIWALI
#3.  lower
print(string.lower())
#4. Remove White space from, beginning or end
a=" hello   "
print(a)
b=a.strip()
print(b)

#5 split()
c="hello,world"
print(c.split(",")) 
d= "hello.world"
print(d.split("."))
e="hello world"
print(e.split(" "))
print(e.split("d"))



#6.capitalize()
name="mansi is "
print(name.capitalize())

#7 find
print(name.find("s"))

#8 title
print(name.title())

#9 replace()
n="mensi"
print(n.replace("e","a"))

#10.check 
#a isndecimal()
s="1"
p=s.isdigit()
print(p)

#isalpha()
print(n.isalpha())
