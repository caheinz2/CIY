import peripherals.heap as heap
import peripherals.churches as churches
import peripherals.buildings as buildings
import math




#given a list of churches, turns them into a max priority queue.
def churchHeap(array):
    retVal = heap.heap()
    retVal.heapify(array)
    return retVal

#given a church max priority queue and a sorted array of buildings, finds the best one to put the top church in.
#as of now, the best fit is defined to be the first possible fit.
def findBestFit(church, buildings, gender):
    for building in buildings:
        if canFit(church, building, gender):
            return building

    #RAISE ERROR! CHURCH CAN'T FIT ANYWHERE
    return

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
    capacity = building.getTotalCap()

    #Too many people
    if people > capacity:
        return False #"Too Many People"

    #Not enough rooms for adult/student seperation, also 2 adults per room
    adult_floors = building.adult_distribution(church.getAdultRooms(gender), [0])
    lost_capacity = adultCost(adults, building, adult_floors)

    if capacity < people + lost_capacity:
        return False #"Not Enough Student Rooms"

    #else the church can fit
    return True

#determines the capacity lost due to housing adults. EG if 2 adults are housed in a 3 person room, this fn returns 1
def adultCost(adults, building, adult_floors):
    lost_capacity = adults % 2 #if odd number of adults, one more spot is lost

    for pair in adult_floors:
        floor = building.getFloor(pair[0])
        rooms = floor.minRooms(pair[1])
        lost_capacity += sum(rooms) - (pair[1] * 2)

    return lost_capacity
