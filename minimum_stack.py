class MinStack:

    def __init__(self):
        self.arr = []
        self.length = 0 #nice to have
        self.current_min = 0 #not necessary
        self.minimums = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        #key
        val = min(val, self.minimums[-1] if self.minimums else val)
        self.minimums.append(val)

    def pop(self) -> None:
        self.arr.pop()
        self.minimums.pop()
        
    def top(self) -> int:
        return self.arr[-1]
        
    def getMin(self) -> int:
        return self.minimums[-1]

        
