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

building_heap = heap.heap()
building_heap.heapify(building_list)

#for building in building_list:
#    print(building)

#for church in church_list:
#    print(church)

#print(church_heap.isEmpty())
#print(building_heap.isEmpty())
while not church_heap.isEmpty() and not building_heap.isEmpty():
    cur_church = church_heap.pop()

    if cur_church.getMaleStudents() - cur_church.getHousedMaleStudents() > 0:
        male_best_building = main_fns.findBestFit(cur_church, building_heap, "Male")
        a_list = male_best_building.addChurch(cur_church, "Male")
        cur_church.addBuilding(a_list)
        if male_best_building.getVacantCap() > 3:
            building_heap.push(male_best_building)

    if cur_church.getFemaleStudents() - cur_church.getHousedFemaleStudents() > 0:
        female_best_building = main_fns.findBestFit(cur_church, building_heap, "Female")
        b_list = female_best_building.addChurch(cur_church, "Female")
        cur_church.addBuilding(b_list)
        if female_best_building.getVacantCap() > 3:
            building_heap.push(female_best_building)

    if cur_church.getTotal() - cur_church.getHousedTotal() > 0:
        church_heap.push(cur_church)

if building_heap.isEmpty() and not church_heap.isEmpty():
    print("NOT ALL CHURCHES FIT")

else:
    print("----------BUILDING LIST----------")
    for building in building_list:
        print(building)
        building.printChurches()
        print()

    print("----------CHURCH LIST----------")
    for church in church_list:
        print(church)
        church.printBuildings()
        print()


print("Total Lost Capacity is: {}".format(main_fns.totalCost(church_list, building_list)))
