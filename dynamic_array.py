class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity
    #O(1)
    def get(self, i: int) -> int:
        return self.arr[i]
    #O(1)
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
    #O(n)
    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.arr[self.length] = n
        self.length += 1
    #O(1)
    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.arr[self.length]
 
    #O(n)
    def resize(self) -> None:
        extra = [None] * self.capacity
        self.capacity = 2 * self.capacity
        self.arr = self.arr + extra

    #O(1)
    def getSize(self) -> int:
        return self.length
        
    #O(1)
    def getCapacity(self) -> int:
        return self.capacity
