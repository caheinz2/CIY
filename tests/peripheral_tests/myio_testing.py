import openpyxl
import modules.peripherals.churches as churches
import modules.peripherals.buildings as buildings

#reads data from a .xlsx file in the correct format and returns a list of churches
def input(filename):
    workbook = openpyxl.load_workbook(filename)
    worksheet = workbook['Churches']

    churchList = []

    for row in worksheet:
        if isValidChurch(row):
            curChurch = churches.church(row)
            churchList.append(curChurch)

    buildingList = []

    worksheet = workbook['Buildings']
    for row in worksheet:
        if isValidBuilding(row):
            curBuilding = buildings.building(row)
            buildingList.append(curBuilding)

    retList = [churchList, buildingList]
    return retList


#returns true if church is valid
def isValidChurch(input):
    if type(input[4].value) == int: #assume that if female_adults input is an int then church is valid
        return True
    else:
        return False

#returns true if building is valid
def isValidBuilding(input):
    if type(input[1].value) == int: #assume that if room 1 capacity is an int then building is valid
        return True
    else:
        return False
