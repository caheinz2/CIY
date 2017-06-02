class building:
    def __init__(self, info):
        self.name = info[0].value
        self.room1 = (info[1].value, info[2].value)
        self.room2 = (info[3].value, info[4].value)
        self.room3 = (info[5].value, info[6].value)
        self.room4 = (info[7].value, info[8].value)
        self.gender = info[9].value

        if type(self.room2[0]) != int:
            self.room2 = (0,0)
        if type(self.room3[0]) != int:
            self.room3 = (0,0)
        if type(self.room4[0]) != int:
            self.room4 = (0,0)


    def __str__(self):
        print(self.name)
        print("    Room 1 Quantity: {} Capacity: {}".format(self.room1[0], self.room1[1]))
        print("    Room 2 Quantity: {} Capacity: {}".format(self.room2[0], self.room2[1]))
        print("    Room 3 Quantity: {} Capacity: {}".format(self.room3[0], self.room3[1]))
        print("    Room 4 Quantity: {} Capacity: {}".format(self.room4[0], self.room4[1]))
        print("    Gender: {}".format(self.gender))
        return "\n"

    #call these functions to get important data

    def getRoom1Total(self):
        return self.room1[0] * self.room1[1]

    def getRoom2Total(self):
        return self.room2[0] * self.room2[1]

    def getRoom3Total(self):
        return self.room3[0] * self.room3[1]

    def getRoom4Total(self):
        return self.room4[0] * self.room4[1]

    def getTotal(self):
        return self.getRoom1Total() + self.getRoom2Total() + self.getRoom3Total() + self.getRoom4Total()

    #helper functions

    #comparison overloads
    def __lt__(self, other):
        return self.getTotal() < other.getTotal()

    def __gt__(self, other):
        return self.getTotal() > other.getTotal()
