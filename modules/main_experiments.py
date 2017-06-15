import peripherals.myio as myio
import peripherals.churches as churches
import peripherals.buildings as buildings
import peripherals.heap as heap
import main_fns


inputList = myio.input('documentation/TN7_Test.xlsx')
churchList = inputList[0]
buildingList = inputList[1]
buildingList.sort()
building_list = heap.heap()
building_list.heapify(buildingList)
buildingList = building_list

#val = main_fns.canFit(churchList[0], buildingList[0], "Female")
#print(val)
#print( )

#val = main_fns.canFit(churchList[0], buildingList[0], "Male")
#print(val)
#print( )

#val = main_fns.canFit(churchList[0], buildingList[1], "Female")
#print(val)
#print( )

#val = main_fns.canFit(churchList[0], buildingList[1], "Male")
#print(val)
#print( )

#val = main_fns.canFit(churchList[0], buildingList[2], "Female")
#print(val)
#print( )

#val = main_fns.canFit(churchList[0], buildingList[2], "Male")
#print(val)
#print( )

#val = main_fns.canFit(churchList[0], buildingList[3], "Female")
#print(val)
#print( )

#val = main_fns.canFit(churchList[0], buildingList[3], "Male")
#print(val)
#print( )


#val = main_fns.canFit(churchList[1], buildingList[0], "Female")
#print(val)
#print( )

#val = main_fns.canFit(churchList[1], buildingList[0], "Male")
#print(val)
#print( )

#val = main_fns.canFit(churchList[1], buildingList[1], "Female")
#print(val)
#print( )

#val = main_fns.canFit(churchList[1], buildingList[1], "Male")
#print(val)
#print( )

#val = main_fns.canFit(churchList[1], buildingList[2], "Female")
#print(val)
#print( )

#val = main_fns.canFit(churchList[1], buildingList[2], "Male")
#print(val)
#print( )

#val = main_fns.canFit(churchList[1], buildingList[3], "Female")
#print(val)
#print( )

#val = main_fns.canFit(churchList[1], buildingList[3], "Male")
#print(val)
#print( )
print(churchList[0], churchList[1])

val = main_fns.findBestFit(churchList[0], buildingList, "Male")
print(val)

val = main_fns.findBestFit(churchList[0], buildingList, "Female")
print(val)

val = main_fns.findBestFit(churchList[1], buildingList, "Male")
print(val)

val = main_fns.findBestFit(churchList[1], buildingList, "Female")
print(val)
