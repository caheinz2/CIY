class building:

    class floor:
        def __init__(self, rooms, capacity):
            self.rooms = rooms
            self.capacity = capacity

        def getCapacity(self):
            return self.capacity

        def getRooms(self):
            return self.rooms



    def __init__(self, info):
        self.name = info[0].value
        self.gender = info[1].value
        self.floors = []

        x = len(info)
        i = 2
        while i < x:
            if type(info[i].value) == int:
                self.floors.append(building.floor(info[i].value, info[i+1].value))
                i += 2
            else:
                break


    def __str__(self):
        print(self.name)
        print("    Number of Floors: {}".format(self.getNumFloors()))
        print("    Total Capacity: {} ".format(self.getTotalCap()))
        print("    Gender: {}".format(self.gender))
        return "\n"

    #call these functions to get important data
    def getNumFloors(self):
        retVal = 0
        for floor in self.floors:
            retVal += 1
        return retVal

    def getFloor(self, floor):
        return self.floors(floor - 1)

    def getTotalCap(self):
        retVal = 0
        for floor in self.floors:
            retVal += floor.getCapacity()
        return retVal

    def getTotalRooms(self):
        retVal = 0
        for floor in self.floors:
            retVal += floor.getRooms()
        return retVal

    def getGender(self):
        return self.gender

    #helper functions

    #comparison overloads
    def __lt__(self, other):
        return self.getTotalCap() < other.getTotalCap()

    def __gt__(self, other):
        return self.getTotal() > other.getTotal()
