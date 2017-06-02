import peripherals.myio as myio
import peripherals.churches as churches
import peripherals.buildings as buildings
import main_fns


inputList = myio.input('documentation/TN7_Test.xlsx')
churchList = inputList[0]
buildingList = inputList[1]
buildingList.sort()

#val = main_fns.canFit(churchList[1], buildingList[0], "Female")
#print(val)

#val = main_fns.canFit(churchList[0], buildingList[0], "Male")
#print(val)

#val = main_fns.canFit(churchList[1], buildingList[2], "Female")
#print(val)

#val = main_fns.canFit(churchList[1], buildingList[0], "Male")
#print(val)

val = main_fns.findBestFit(churchList[0], buildingList, "Male")
print(val)

val = main_fns.findBestFit(churchList[0], buildingList, "Female")
print(val)

val = main_fns.findBestFit(churchList[1], buildingList, "Male")
print(val)

val = main_fns.findBestFit(churchList[1], buildingList, "Female")
print(val)
