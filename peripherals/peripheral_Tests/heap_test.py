from ..heap import heap
from random import randint

#tests heap pop
a  = []
for i in range (10):
    a.append(randint(0,100))
print ("List of data is: ")
print (a)

b = heap()
b.heapify(a)
print("Heap data is: ")
print(b.data)

for i in range(10):
    print(b.pop())

#tests heap push
c = []
for i in range(10):
    c.append(randint(0,100))

print(c)
for element in c:
    b.push(element)
    print ("Added Element: ", element)
    print("Resulting heap: ", b.data)
