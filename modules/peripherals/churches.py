#Class structure for storing information about churches.

class church:
    def __init__(self, info):
        self.name = info[0].value
        self.city = info[1].value
        self.state = info[2].value
        self.zipcode = str(info[3].value)
        self.female_adults = info[4].value
        self.female_students = info[5].value
        self.female_children = info[6].value
        self.male_adults = info[7].value
        self.male_students = info[8].value
        self.male_children = info[9].value
        self.housed_female_adults = 0
        self.housed_female_students = 0
        self.housed_female_children = 0
        self.housed_male_adults = 0
        self.housed_male_students = 0
        self.housed_male_chidlren = 0
        self.contact = (info[16].value, info[17].value, info[18].value, info[19].value)
        self.buildings = []

        if type(self.female_children) == str:
            self.female_children = 0
        if type(self.male_children) == str:
            self.male_children = 0

    def __str__(self):
        print(self.name)
        print( "    Address: " + self.city +  ", " + self.state + ", " + self.zipcode)
        print("    Adults: {} males and {} females".format(self.male_adults, self.female_adults))
        print("    Students: {} males and {} females".format(self.male_students, self.female_students))
        #print("    Children: {} males and {} females".format(self.male_children, self.female_children))
        print("    Contact Information: {} {} {} {}".format(self.contact[0], self.contact[1], self.contact[2], self.contact[3]))

        return "\n"

    #call these functions to get/set important data.
    def getFemales(self):
        return self.female_adults + self.female_students #+ self.female_children

    def getMales(self):
        return self.male_adults + self.male_students #+ self.male_children

    def getAdults(self):
        return self.female_adults + self.male_adults

    def getMaleAdults(self):
        return self.male_adults

    def getHousedMaleAdults(self):
        return self.housed_male_adults

    def setHousedMaleAdults(self, number):
        if number > self.male_adults:
            number = self.male_adults
        self.housed_male_adults = number

    def getFemaleAdults(self):
        return self.female_adults

    def getHousedFemaleAdults(self):
        return self.housed_female_adults

    def setHousedFemaleAdults(self, number):
        if number > self.female_adults:
            number = self.female_adults
        self.housed_female_adults = number

    def getStudents(self):
        return self.female_students + self.male_students

    def getMaleStudents(self):
        return self.male_students

    def getHousedMaleStudents(self):
        return self.housed_male_students

    def setHousedMaleStudents(self, number):
        if number > self.male_students:
            number = self.male_students
        self.housed_male_students = number

    def getFemaleStudents(self):
        return self.female_students

    def getHousedFemaleStudents(self):
        return self.housed_female_students

    def setHousedFemaleStudents(self, number):
        if number > self.female_students:
            number = self.female_students
        self.housed_female_students = number

    def getChildren(self):
        return self.female_children + self.male_children

    def getTotal(self):
        return self.female_adults + self.female_students + self.male_adults + self.male_students #+ self.female_children + self.male_children

    def getHousedTotal(self):
        return self.housed_male_adults + self.housed_female_adults + self.housed_male_students + self.housed_female_students

    def getContactName(self):
        return self.contact[0] + " " + self.contact[1]

    def getContactEmail(self):
        return self.contact[2]

    def getContactCell(self):
        return self.contact[3]

    def getName(self):
        return self.name

    def getAddress(self):
        return self.city + " " + self.state

    def getAdultRooms(self, gender):
        if gender == "Male":
            return int(self.getMaleAdults() / 2) + self.getMaleAdults() % 2 #2 adults per room
        else:
            return int(self.getFemaleAdults() / 2) + self.getFemaleAdults() % 2

    def getBuildings(self):
        return self.buildings

    #helper functions

    def addBuilding(self, list): #[building, floor # 1 number, floor # 1 adults, floor # 1 students, etc]
        self.buildings.append(list)

        #update housed people
        gender = list[0].getGender()
        i = 1
        while i < len(list):
            if gender == "Male":
                self.setHousedMaleAdults(self.getHousedMaleAdults() + list[i+1])
                self.setHousedMaleStudents(self.getHousedMaleStudents() + list[i+2])
            else:
                self.setHousedFemaleAdults(self.getHousedFemaleAdults() + list[i+1])
                self.setHousedFemaleStudents(self.getHousedFemaleStudents() + list[i+2])
            i += 3

    def printBuildings(self):
        for building in self.buildings:
            print("    {}".format(building[0].getName()))
            print("        {} Dorm".format(building[0].getGender()))
            floors = building[1:]
            i = 0
            while i < len(floors):
                if(floors[i+1] != 0 or floors[i+2] != 0):
                    print("        Floor {}: {} adults and {} students".format(floors[i], floors[i+1], floors[i+2]))
                i += 3
            print()



    #comparison overloads
    def __lt__(self, other):
        return self.getTotal() < other.getTotal()

    def __gt__(self, other):
        return self.getTotal() > other.getTotal()
