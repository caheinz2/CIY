import peripherals.heap as heap
import peripherals.churches as churches
import peripherals.buildings as buildings
import math


#given a church max priority queue and a building min priority queue, finds the best one to put the top church in.
#as of now, the best fit is defined to be the first possible fit.
def findBestFit(church, building_heap, gender):
    temp = [] #used to store buildings that will be pushed back to the heap
    retVal = "Error: No buildings can fit church"
    temp_retVal = retVal
    #print(church, gender)
    while not building_heap.isEmpty():
        cur_building = building_heap.pop()
        temp.append(cur_building)
        #print(cur_building)

        can_fit = canFit(church, cur_building, gender)
        #print(can_fit)
        #If entire church can fit in the current building and the current building's gender has been assigned, return it.
        if can_fit and cur_building.getGender() == gender:
            retVal = cur_building
            break

        #If entire church can fit but gender hasn't been assigned, check if it is the best unassigned fit
        elif can_fit and type(retVal) == str:
            retVal = cur_building

        #If church doesn't fit but the building is compatable, save it in case no better building is found
        elif not can_fit and type(temp_retVal) == str and (cur_building.getGender() == gender or cur_building.getGender() == "Unassigned"):
            temp_retVal = cur_building

        elif not can_fit and cur_building.getGender() == gender:
            temp_retVal = cur_building

        elif not can_fit and cur_building.getGender() == "Unassigned" and temp_retVal.getGender() == "Unassigned":
            temp_retVal = cur_building

    if type(retVal) == str and type(temp_retVal) != str:
        retVal = temp_retVal

    if type(retVal) != str:
        temp.remove(retVal)
        for item in temp:
            building_heap.push(item)

    return retVal

#returns true if church can fit in building
def canFit(church, building, gender):

    #Gender mismatch
    if gender == "Male":
        if building.getGender() == "Female":
            return False #"Gender Mismatch"
        students = church.getMaleStudents()
        adults = church.getMaleAdults()

    if gender == "Female":
        if building.getGender() == "Male":
            return False #"Gender Mismatch"
        students = church.getFemaleStudents()
        adults = church.getFemaleAdults()

    people = students + adults
    capacity = building.getVacantCap()

    #Too many people
    if people > capacity:
        return False #"Too Many People"

    #Not enough rooms for adult/student seperation, also 2 adults per room
    adult_floors = building.adult_distribution(church, gender)
    lost_capacity = building.adultCost(adults, adult_floors)

    if capacity < people + lost_capacity:
        return False #"Not Enough Student Rooms"

    #else the church can fit
    return True

#computes the total empty spaces over the whole campus
def totalCost(church_list, building_list):
    retVal = 0
    for building in building_list:
        retVal += building.getTotalCap() - building.getVacantCap()

    for church in church_list:
        retVal -= church.getTotal()
    return retVal
