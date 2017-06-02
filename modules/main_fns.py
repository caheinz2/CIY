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
            return False #"Gender Mistmatch"
        students = church.getMaleStudents()
        adults = church.getMaleAdults()

    if gender == "Female":
        if building.getGender() == "Male":
            return False #"Gender Mismatch"
        students = church.getFemaleStudents()
        adults = church.getFemaleAdults()

    people = students + adults
    rooms = building.getTotalRooms()
    capacity = building.getTotalCap()

    #Too many people
    if people > capacity:
        return False #"Too Many People"

    #Not enough rooms for adult/student seperation
    adult_rooms = int(math.ceil(adults / 2))
    student_rooms = rooms - adult_rooms
    needed_rooms = int(math.ceil(students/(capacity/rooms)))
    if needed_rooms > student_rooms:
        return False #"Not Enough Student Rooms"

    #else the church can fit
    return True
