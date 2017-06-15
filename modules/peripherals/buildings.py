class building:

    class floor:
        def __init__(self, rooms):
            self.rooms = []
            i = 0
            while i < len(rooms):
                self.rooms.append([rooms[i], rooms[i+1]]) #self is a list of capacity/quantity room pairs.
                                                          #items in this list are assumed to be vacant.
                i += 2

            self.total_rooms = self.rooms #includes all rooms (vacant and occupied)
            self.total_capacity = sum(self.expandRooms())

        #returns the total vacant capacity of the floor
        def floorCapacity(self):
            retVal = 0
            i = 0
            for pair in self.rooms:
                retVal += pair[0] * pair[1]

            return retVal

        def getRooms(self):
            return self.rooms

        def setRooms(self, rooms):
            self.rooms = rooms

        #translates rooms list from capacity/quantity format to list of capacities eg [2,3] ==> [2,2,2]
        def expandRooms(self):
            rooms = self.getRooms()
            retVal = []
            i = 0
            for pair in self.rooms:
                for i in range(pair[1]):
                    retVal.append(pair[0])

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
        self.churches = []

    def __str__(self):
        print(self.name)
        print("    Number of Floors: {}".format(self.getNumFloors()))
        print("    Total Capacity: {} ".format(self.getTotalCap()))
        print("    Occupied Capacity: {} ".format(self.getTotalCap() - self.getVacantCap()))
        print("    Gender: {}".format(self.gender))
        return "\n"


    #call these functions to get/set important data
    def getNumFloors(self):
        return len(self.floors)

    def getFloor(self, floor_number): #floor_number must be at > 1
        return self.floors[floor_number - 1]

    def getVacantCap(self):
        retVal = 0
        for floor in self.floors:
            retVal += floor.floorCapacity()
        return retVal

    def getTotalCap(self):
        retVal = 0
        for floor in self.floors:
            retVal += floor.total_capacity
        return retVal

    def getGender(self):
        return self.gender

    def setGender(self, gender): #raise error if not "Male", "Female", or "Unassigned"
        self.gender = gender

    def getName(self):
        return self.name

    def getChurches(self): #list of [church, floor number 1 adults/ rooms, floor 1 students/ rooms, floor 2 adult rooms, etc]
        return self.churches


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

    #distributes adult rooms while considering number of students on each floor
    #returns a list of pairs of floor / number of rooms per floor
    def adult_distribution(self, church, gender):

        floor_numbers = []
        for i in range (self.getNumFloors()):
            floor_numbers.append(i + 1)

        if gender == "Male":
            num_unhoused_students = church.getMaleStudents() - church.getHousedMaleStudents()
            num_students = church.getMaleStudents()
        else:
            num_unhoused_students = church.getFemaleStudents() - church.getHousedFemaleStudents()
            num_students = church.getFemaleStudents()

        distribution = []
        completed = 0
        adult_rooms = church.getAdultRooms(gender)

        i = 0
        while num_unhoused_students > 0 and i < len(floor_numbers):
            cur_floor = self.getFloor(floor_numbers[i])
            cur_adults = min(cur_floor.floorCapacity(), num_unhoused_students) * adult_rooms / num_students
            cur_adults = int(cur_adults)

            if cur_adults == 0 and (adult_rooms - completed > 1 or num_unhoused_students == 0) and cur_floor.floorCapacity() > 3:
                cur_adults += 1
            distribution.append([floor_numbers[i], cur_adults])
            completed += cur_adults
            num_unhoused_students -= cur_floor.floorCapacity() - sum(cur_floor.minRooms(cur_adults))
            i += 1

        if num_unhoused_students <= 0:
            distribution[-1][1] += (adult_rooms - completed) #last floor has all remaining adult rooms...if all students are housed. REVISE THIS LATER?
        return distribution #list of [floor number, adult rooms on floor] pairs

    #determines the capacity lost due to housing adults. EG if 2 adults are housed in a 3 person room, this fn returns 1
    def adultCost(self, adults, adult_floors):
        lost_capacity = adults % 2 #if odd number of adults, one more spot is lost

        for pair in adult_floors:
            floor = self.getFloor(pair[0])
            rooms = floor.minRooms(pair[1])
            lost_capacity += sum(rooms) - (pair[1] * 2)

        return lost_capacity

    #Adds a church to the building. Fills floors from the bottom up.
    #Updates building stats
    #Marks in the church building information.
    #Gender should be compatable with building and will update the building gender (if it is unassigned)
    def addChurch(self, church, gender, simulate):
        if gender == "Male":
            num_unhoused_students = church.getMaleStudents() - church.getHousedMaleStudents()
        else:
            num_unhoused_students = church.getFemaleStudents() - church.getHousedFemaleStudents()
        if not simulate:
            self.setGender(gender)

        adult_floors = self.adult_distribution(church, gender)
        church_list = [self] #list to add to church
        building_list = [church] #list to add to building
        cost = 0

        for pair in adult_floors:
            cur_floor = self.getFloor(pair[0])
            rooms = cur_floor.expandRooms()
            num_adult_rooms = pair[1]
            type_adult_rooms = cur_floor.minRooms(num_adult_rooms)
            cost += sum(type_adult_rooms) - (2 * num_adult_rooms)

            for item in type_adult_rooms:
                rooms.remove(item)

            type_student_rooms = self.fillRooms(num_unhoused_students, rooms)

            #update rooms
            for item in type_student_rooms:
                rooms.remove(item)

            #format type_x_rooms and rooms and push them to the list
            cur_floor_students = sum(type_student_rooms)
            num_unhoused_students -= cur_floor_students

            rooms = self.formatRooms(rooms)
            type_adult_rooms = self.formatRooms(type_adult_rooms)
            type_student_rooms = self.formatRooms(type_student_rooms)

            if not simulate:
                cur_floor.setRooms(rooms)
                church_list.append(pair[0])
                church_list.append(num_adult_rooms * 2)
                church_list.append(cur_floor_students)

                building_list.append(pair[0])
                building_list.append(type_adult_rooms)
                building_list.append([cur_floor_students, type_student_rooms])

        cost += abs(num_unhoused_students)

        if not simulate:
            self.churches.append(building_list)

        if simulate:
            return cost


        return church_list


    #helper functions
    def addFloor(self, info):
        rooms = []
        for cell in info:
            if type(cell.value) == int:
                rooms.append(cell.value)
        f = building.floor(rooms)
        self.floors.append(f)

    def formatRooms(self, expanded_list):
        retVal = []
        finished = []
        for item in expanded_list:
            if item not in finished:
                finished.append(item)
                retVal.append([item, expanded_list.count(item)])

        return retVal

    #returns a list of rooms that the students will occupy.
    def fillRooms(self, num_unhoused_students, rooms):
        if rooms == []:
            return []

        if num_unhoused_students < rooms[0]:
            return [rooms[0]]

        else:
            retVal = self.fillRoomsRecursive(num_unhoused_students, rooms)
            return retVal[:-1]

    def fillRoomsRecursive(self, num_unhoused_students, rooms):
        if num_unhoused_students <= 0:
            return [num_unhoused_students]
        elif len(rooms) == 0:
            return [-100]
        else:
            retVal = []
            t = len(rooms)
            for i in range(t):
                curVal = self.fillRoomsRecursive(num_unhoused_students - rooms[-(i+1)], rooms[:-(i+1)])
                curVal.insert(0, rooms[-(i+1)])

                if retVal == [] or curVal[-1] > retVal[-1]:
                    retVal = curVal
                if retVal[-1] == 0:
                    break
        return retVal


    def printChurches(self):
        for item in self.churches:
            church = item[0]
            print("    {} from {}".format(church.getName(), church.getAddress()))
            i = 1
            while i < len(item):
                if item[i+1] != [] or item[i+2][0] != 0:
                    print("        floor {}: ".format(item[i]))
                    for adults in item[i + 1]:
                        print("            {} adult rooms from {}-person rooms".format(adults[1], adults[0]))
                    for students in item[i + 2][1]:
                        print("            {} {}-person student rooms".format(students[1], students[0]))
                i += 3
            print()

        print()

    #comparison overloads. These are reversed on purpose because I want a min heap for them (not a max heap)
    def __lt__(self, other):
        return self.getVacantCap() > other.getVacantCap()

    def __gt__(self, other):
        return self.getVacantCap() < other.getVacantCap()

    def __eq__(self, other):
        return self.name == other.name
