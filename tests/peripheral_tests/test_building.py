import modules.peripherals.heap as heap
import tests.peripheral_tests.myio_testing as myio

#tests heap made of churches
def test_heap_church():
    buildingList = myio.input('documentation/TN7_Test.xlsx')[1]
    building_heap = heap.heap()
    building_heap.heapify(buildingList)
    a = []

    while not building_heap.isEmpty():
        a.append(building_heap.pop().getTotal())

    b = a
    b.sort()
    assert a == b
