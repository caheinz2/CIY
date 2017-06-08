import main_fns
import peripherals.churches as churches
import peripherals.buildings as buildings
import peripherals.myio as myio
import peripherals.heap as heap

input_list = myio.input('documentation/TN7_Test.xlsx')
church_list = input_list[0]
building_list = input_list[1]
building_list.sort()


church_heap = heap.heap()
church_heap.heapify(church_list)

while not church_heap.isEmpty():
    cur_church = church_heap.pop()

    male_best_building = main_fns.findBestFit(cur_church, building_list, "Male")
    female_best_building = main_fns.findBestFit(cur_church, building_list, "Female")

    a_list = male_best_building.addChurch(cur_church, "Male")
    b_list = female_best_building.addChurch(cur_church, "Female")

    cur_church.addBuilding(a_list)
    cur_church.addBuilding(b_list)


    if cur_church.getTotal() - cur_church.getHousedTotal() > 0:
        church_heap.push(cur_church)

for building in building_list:
    print(building)
    building.printChurches()
    print()
    print()
