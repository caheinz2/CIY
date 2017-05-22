class heap:
    def __init__(self):
        self.data = []

    #creates a new heap by sorting an array
    def heapify(self, array):
        self.data = list(array)
        self.data.sort(reverse = True)
        self.data.insert(0, -1) #actual heap data starts at index 1.
   
    #pops the maximum value off the heap
    def pop(self):
        retVal = self.data[1]
        self.swap(1, len(self.data) - 1)
        self.data.pop(len(self.data) - 1) #removes last spot from list
        self.heapifyDown(1)
        return retVal

    #pushes a value to the heap
    def push(self, value):
        self.data.append(value)
        self.heapifyUp(len(self.data) - 1)
        

    #returns if the heap has data in it or not
    def isEmpty(self):
        if len(self.data) > 1:
            return False
        return True

    

    #helper functions

    def heapifyUp(self, position):
        if position == 1:
            return
        if self.data[position] > self.data[self.parent(position)]:
            self.swap(position, self.parent(position))
            self.heapifyUp(self.parent(position))


    def heapifyDown(self, position):
        if self.numChildren(position) == 2:
            right = self.rightChild(position)
            left = self.leftChild(position)
            if max(self.data[right], self.data[left]) > self.data[position]:
                if self.data[right] > self.data[left]:
                    self.swap(position, right)
                    self.heapifyDown(right)
                else:
                    self.swap(position, left)
                    self.heapifyDown(left)
        
        elif self.numChildren(position) == 1:
            if self.data[self.leftChild(position)] > self.data[position]:
                self.swap(position, self.leftChild(position))
                self.heapifyDown(self.leftChild(position))
        
                
    #swaps the data at two indices
    def swap(self, index1, index2):
        temp = self.data[index1]
        self.data[index1] = self.data[index2]
        self.data[index2] = temp

    #finds the parent of a given index
    def parent(self, index):
        return int(index / 2)

    #finds the right child of a given index
    def rightChild(self, index):
        return int(index) * 2 + 1

    #finds the left child of a given index
    def leftChild(self, index):
        return int(index) * 2

    #returns the number of children an index has
    def numChildren(self, index):
        length = len(self.data)
        retVal = 0
        if self.rightChild(index) < length:
            retVal += 1
        if self.leftChild(index) < length:
            retVal += 1
        return retVal

      
