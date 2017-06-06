class building:

    class floor:
        def __init__(self, rooms):
            self.rooms = rooms #rooms is a list where every odd number is the capacity
                               #of a room type and the even numbers are the number of rooms of each type.

        #returns the total capacity of the floor
        def floorCapacity(self):
            retVal = 0
            i = 0
            while i < len(self.rooms):
                retVal += (self.rooms[i] * self.rooms[i+1])
                i += 2

            return retVal

        def getRooms(self):
            return self.rooms

        #translates rooms list from capacity/quantity format to list of capacities eg [2,3] ==> [2,2,2]
        def expandRooms(self):
            rooms = self.getRooms()
            retVal = []
            i = 0
            while i < len(rooms):
                for x in range(rooms[i+1]):
                    retVal.append(rooms[i])
                i += 2

            retVal.sort()
            return retVal


        #returns a list of the [number] smallest room capacities.
        def minRooms(self, number):
            retVal = []
            rooms = self.expandRooms()
            if len(rooms) <= number:
                retVal = rooms

            else:
                retVal = rooms[0:number]

            return retVal


    def __init__(self, info):
        self.name = info[0].value
        self.gender = info[1].value
        self.floors = []

    def __str__(self):
        print(self.name)
        print("    Number of Floors: {}".format(self.getNumFloors()))
        print("    Total Capacity: {} ".format(self.getTotalCap()))
        print("    Gender: {}".format(self.gender))
        return "\n"

    def addFloor(self, info):
        rooms = []
        for cell in info:
            if type(cell.value) == int:
                rooms.append(cell.value)
        f = building.floor(rooms)
        self.floors.append(f)

    #distributes adult rooms while considering floor weight.
    #returns a list of pairs of floor / number of rooms per floor
    #floor_numbers is a list of the floors wanted or 0 for all
    def adult_distribution(self, adult_rooms, floor_numbers):
        floor_capacity = self.getFloorCapacities(floor_numbers)
        distribution = []
        total_capacity = sum(floor_capacity)
        completed = 0

        for i in range(len(floor_capacity) - 1):
            cur_floor = floor_numbers[i]
            cur_adults= floor_capacity[i] * adult_rooms / total_capacity #weighted number of adult rooms on given floor
            cur_adults = int(cur_adults)
            if cur_adults == 0 and adult_rooms - completed > 1:
                cur_adults += 1
            distribution.append([cur_floor, cur_adults])
            completed += cur_adults

        distribution.append([floor_numbers[-1], adult_rooms - completed]) #last floor has all remaining adult rooms. REVISE THIS LATER
        return distribution

    #call these functions to get important data
    def getNumFloors(self):
        return len(self.floors)

    def getFloor(self, floor_number): #floor_number must be at > 1
        return self.floors[floor_number - 1]

    def getTotalCap(self):
        retVal = 0
        for floor in self.floors:
            retVal += floor.floorCapacity()
        return retVal

    def getGender(self):
        return self.gender

    #returns a list of all floor capacities listed in the floor_numbers list.
    #if floor_numbers is 0, returns floor capacities for all floors.
    def getFloorCapacities(self, floor_numbers):
        if floor_numbers[0] == 0: #handles 0 as input
            for i in range (self.getNumFloors()):
                    floor_numbers.append(i + 1)
            floor_numbers.remove(0)

        floor_capacity = []
        for item in floor_numbers:
            floor_capacity.append(self.getFloor(item).floorCapacity()) #put the capacities of the given floors in floor_capacity

        return floor_capacity


    #helper functions

    #comparison overloads
    def __lt__(self, other):
        return self.getTotalCap() < other.getTotalCap()

    def __gt__(self, other):
        return self.getTotal() > other.getTotal()
