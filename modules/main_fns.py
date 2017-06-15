import peripherals.heap as heap
import peripherals.churches as churches
import peripherals.buildings as buildings
import math


#given a church max priority queue and a building min priority queue, finds the best one to put the top church in.
#as of now, the best fit is defined to be the first possible fit.
def findBestFit(church, building_list, gender):
    best_so_far = None
    cost_so_far = 1000

    for cur_building in building_list:
        cost = 0
        if not canFit(church, cur_building, gender):
            cost += 15
        if cur_building.getGender() == "Unassigned":
            cost += 15
        if cur_building.getGender() == gender or cur_building.getGender() == "Unassigned":

            cost += cur_building.addChurch(church, gender, True)

            if cost < cost_so_far:
                best_so_far = cur_building
                cost_so_far = cost

    return best_so_far

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

#computes the minimum total adult cost
def minAdultCost(church_list):
    retVal = 0
    for church in church_list:
        retVal += church.getMaleAdults() % 2
        retVal += church.getFemaleAdults() % 2

    return retVal

def actualAdultCost(church_list, building_list):
    return totalCost(church_list, building_list) - actualStudentCost(church_list, building_list)

def actualStudentCost(church_list, building_list):
    housed_students = 0
    total_students = 0
    for building in building_list:
        churches = building.getChurches()
        for church in churches:
            i = 3
            while i < len(church):
                housed_students += church[i][0]
                i += 3
    for church in church_list:
        total_students += church.getStudents()

    return housed_students - total_students
