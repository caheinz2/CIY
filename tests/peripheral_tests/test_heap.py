import modules.peripherals.heap as heap
import random

#tests heap pop
def test_pop():
    a  = []
    for i in range (50):
        a.append(random.randint(0,100))

    b = heap.heap()
    b.heapify(a)

    c = []
    for i in range(50):
        element = b.pop()
        c.append(element)

    a.sort(reverse = True)
    assert a == c

#tests heap push
def test_push():
    d = []
    for i in range(50):
        d.append(random.randint(0,100))

    b = heap.heap()
    b.heapify(d)

    for element in d:
        b.push(element)
        assert max(b.data) == b.data[1]


