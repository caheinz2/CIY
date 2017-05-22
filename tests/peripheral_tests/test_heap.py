import modules.peripherals.heap as heap
import random

#tests heap pop
a  = []
for i in range (10):
    a.append(random.randint(0,100))

b = heap.heap()
b.heapify(a)

c = []
for i in range(10):
    element = b.pop()
    c.append(element)

a.sort(reverse = True)
assert a == c

#tests heap push
d = []
for i in range(10):
    d.append(random.randint(0,100))

for element in d:
    b.push(element)
    assert max(b.data) == b.data[1]


