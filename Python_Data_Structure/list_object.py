# creat list
a = [] # empty list
a = [1] # list with single int element
a = [1, 2, 3, 4] # list with multiple int element
a = [1, '1'] # list with int,str element

# append elemtn to list
a = []
print(a)
a.append(1)
a.append(2)
a.append(3)
print(a)

# insert element to list
a = [1, 2, 3]
print(a)
a.insert(0,"a") # insert "a" at the index of 0
a.insert(3,"b")
print(a)

# extend() stick the list you pass at the end of original list
a = [7, 8, 9]
b = [3, 4, 5]
a.extend(b)
print(a)

# accessing element of list
a = [7, 8, 9]
a[0] # access the first elemtn
a[0:2] # acceess the 0-2 elements
a[1:] # access the element from the second index to the end

# change individual element
a = [1, 2, 3, 4, 5, 6, 7]
a[-1] = 9999
print(a)

# interate each element
for element in a: # option 1
    print(element)

for i in range(len(a)): # option 2 using index
    print(a[i])

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
for elem_a, elem_b in zip(a, b):
    print("%d,%d"%(elem_a, elem_b)) # %d specifies an integer

# delete element
a = [1, 2, 3, 4]
print(a)
del(a[0])
print(a)

# pop()
a = [1, 2, 3, 4]
print(a.pop())
print(a)

# index(): return index
a = ['a', 'b', 'ab', 'c', 'd']
a.index('ab')

# sort()
a = [4, 3, 2, 1]
a.sort()
print(a)

# reverse()
a = [1,2,3,4]
a.reverse() # optin 1
print(a)

a = [1,2,3,4]
print(a[::-1]) # option 2

# 
def f(x):
    return x**5 + 2

b = [9, 3, 5, 6, 8, 10, 7, 4]
a = [f(i) for i in b]
print(a)

# count()
a = [1, 2, 3, 4, 4]
a.count(4)


# store any data structure to list
class example:
    def __init__(self):
        self.value = 10

a = []
for _ in range(5):
    new_example = example()
    a.append(new_example)

print(a) # 现在的a里面存了5个在不同内存地址的实例