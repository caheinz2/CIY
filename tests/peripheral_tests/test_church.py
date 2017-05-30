import modules.peripherals.heap as heap
import tests.peripheral_tests.myio_testing as myio

#tests heap made of churches
def test_heap_church():
    churchList = myio.input('documentation/TN7_Test.xlsx')[0]
    church_heap = heap.heap()
    church_heap.heapify(churchList)
    a = []

    while not church_heap.isEmpty():
        a.append(church_heap.pop().getTotal())

    b = a
    b.sort()
    assert a == b
