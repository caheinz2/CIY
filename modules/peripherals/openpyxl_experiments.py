#from openpyxl import load_workbook
import openpyxl
import myio
import churches

#wb = openpyxl.load_workbook(filename = 'documentation/TN7_Test.xlsx')

#for worksheet in wb:
#    for row in worksheet:
#        for item in row:
#            print(item.value)

churchList = myio.input('documentation/TN7_Test.xlsx')

for church in churchList:
    print (church)
