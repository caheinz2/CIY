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

            return retVal


        #returns a list of the [number] smallest room capacities.
        def minRooms(self, number):
            retVal = []
            rooms = self.expandRooms
            if len(rooms) > number:
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

    #call these functions to get important data
    def getNumFloors(self):
        return len(self.floors)

    def getFloor(self, floor):
        return self.floors(floor - 1)

    def getTotalCap(self):
        retVal = 0
        for floor in self.floors:
            retVal += floor.floorCapacity()
        return retVal

    def getGender(self):
        return self.gender

    #helper functions

    #comparison overloads
    def __lt__(self, other):
        return self.getTotalCap() < other.getTotalCap()

    def __gt__(self, other):
        return self.getTotal() > other.getTotal()
