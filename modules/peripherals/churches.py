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
        self.contact = (info[16].value, info[17].value, info[18].value, info[19].value)

        if type(self.female_children) == str:
            self.female_children = 0
        if type(self.male_children) == str:
            self.male_children = 0

    def __str__(self):
        print(self.name)
        print( "    Address: " + self.city +  ", " + self.state + ", " + self.zipcode)
        print("    Adults: {} males and {} females".format(self.male_adults, self.female_adults))
        print("    Students: {} males and {} females".format(self.male_students, self.female_students))
        print("    Children: {} males and {} females".format(self.male_children, self.female_children))
        print("    Contact Information: {} {} {} {}".format(self.contact[0], self.contact[1], self.contact[2], self.contact[3]))

        return "\n"

    #call these functions to get important data.
    def getFemales(self):
        return self.female_adults + self.female_students #+ self.female_children

    def getMales(self):
        return self.male_adults + self.male_students #+ self.male_children

    def getAdults(self):
        return self.female_adults + self.male_adults

    def getMaleAdults(self):
        return self.male_adults

    def getFemaleAdults(self):
        return self.female_adults

    def getStudents(self):
        return self.female_students + self.male_students

    def getMaleStudents(self):
        return self.male_students

    def getFemaleStudents(self):
        return self.female_students

    def getChildren(self):
        return self.female_children + self.male_children

    def getTotal(self):
        return self.female_adults + self.female_students + self.male_adults + self.male_students #+ self.female_children + self.male_children

    def getContactName(self):
        return self.contact[0] + " " + self.contact[1]

    def getContactEmail(self):
        return self.contact[2]

    def getContactCell(self):
        return self.contact[3]

    def getAdultRooms(self, gender):
        if gender == "Male":
            return int(self.getMaleAdults() / 2) + self.getMaleAdults() % 2 #2 adults per room
        else:
            return int(self.getFemaleAdults() / 2) + self.getFemaleAdults() % 2

    #helper functions

    #comparison overloads
    def __lt__(self, other):
        return self.getTotal() < other.getTotal()

    def __gt__(self, other):
        return self.getTotal() > other.getTotal()
