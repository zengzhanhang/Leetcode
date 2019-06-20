a = "some example string"

# Accessing individual character
a[0]
a[2]
a[-1]

# String 'arithmetic'
a = "abc"
b = "123"

c = a + b
print(c)

# Convert numbers to string: str()
a = 3.1415926
print(type(a))

a = str(a)
print(type(a))

# join()
print(",".join([a,b]))
print(a+b)

# split()
d = ",".join([a,b]) # combine a and b
print(d)
print(d.split(",")) # split d by ","

#read a text file open(filename, 'rb')
"""
open(): 'r' read mode(default), 'b' binary mode, 't' text mode(default)
"""
f = open("D:/Leetcode/Python Data Structure/Toward_artificial_intelligence_that_learns_to_write_code.txt", "rb")
text = f.read().decode('utf-8') # because read file in binary mode, so need to decode

# split whole text to paragrapha
paragraph = text.split('\r\n\r\n')
for p in paragraph:
    print(p)
    print("-" * 60)


# lowercase text or upercase: lower(), upper()
lower = p.lower()
upper = p.upper()

# Capitalize 
cap = lower.capitalize()
cap

# find() find the index of first element 
text.find("the") 

# cound() count how many time the passed character has found
text.count("the") 

# replace() replace element to other element
text.replace("the", "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")

