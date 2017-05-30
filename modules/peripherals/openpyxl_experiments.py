#from openpyxl import load_workbook
import openpyxl
import myio
import churches
import buildings

#wb = openpyxl.load_workbook(filename = 'documentation/TN7_Test.xlsx')

#for worksheet in wb:
#    for row in worksheet:
#        for item in row:
#            print(item.value)

inputList = myio.input('documentation/TN7_Test.xlsx')
churchList = inputList[0]
buildingList = inputList[1]

#for church in churchList:
#    print (church)
for building in buildingList:
    print (building)
