import sys
import modules.main_fns as main_fns
import modules.peripherals.churches as churches
import modules.peripherals.buildings as buildings
import modules.peripherals.myio as myio
import modules.peripherals.heap as heap

filepath = input("Enter path to input file: ")    #program will get input from here and also print output to here
input_list = myio.input(filepath)
church_list = input_list[0]
building_list = input_list[1]
building_list.sort()

church_heap = heap.heap()
church_heap.heapify(church_list)

vacant_building_list = list(building_list)

while not church_heap.isEmpty() and len(vacant_building_list) > 0:
    cur_church = church_heap.pop()

    if cur_church.getMaleStudents() - cur_church.getHousedMaleStudents() > 0:
        male_best_building = main_fns.findBestFit(cur_church, vacant_building_list, "Male")
        a_list = male_best_building.addChurch(cur_church, "Male", False)
        cur_church.addBuilding(a_list)
        if male_best_building.getVacantCap() < 3:
            vacant_building_list.remove(male_best_building)

    if cur_church.getFemaleStudents() - cur_church.getHousedFemaleStudents() > 0:
        female_best_building = main_fns.findBestFit(cur_church, vacant_building_list, "Female")
        b_list = female_best_building.addChurch(cur_church, "Female", False)
        cur_church.addBuilding(b_list)
        if female_best_building.getVacantCap() < 3:
            vacant_building_list.remove(female_best_building)

    if cur_church.getTotal() - cur_church.getHousedTotal() > 0:
        church_heap.push(cur_church)


#Print results to a file
x = 0
remove = 0
for char in filepath:
    x = x + 1
    if char == "/":
        remove = x
filepath = filepath[:remove]

sys.stdout=open(filepath+"output.txt", "w+")

if len(vacant_building_list) == 0 and not church_heap.isEmpty():
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
        print("")


print("Total lost capacity is: {}".format(main_fns.totalCost(church_list, building_list)))
print("Acutal lost capacity due to adults is: {}".format(main_fns.actualAdultCost(church_list, building_list)))
print("Lost capacity due to students is: {}".format(main_fns.actualStudentCost(church_list, building_list)))

sys.stdout.close()
