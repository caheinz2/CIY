import openpyxl
import churches

#reads data from a .xlsx file in the correct format and returns a list of churches
def input(filename):
    workbook = openpyxl.load_workbook(filename)
    worksheet = workbook['MasterList']

    churchList = []

    for row in worksheet:
        if isValidChurch(row):
            curChurch = churches.church(row)
            churchList.append(curChurch)

    return churchList


#returns true if church is valid
def isValidChurch(input):
    if type(input[6].value) == int: #assume that if female_adults input is an int the church is valid
        return True
    else:
        return False
