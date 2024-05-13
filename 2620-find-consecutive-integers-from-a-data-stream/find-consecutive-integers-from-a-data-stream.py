class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value 
        self.k =  k 
        self.deque = deque()
        self.count = 0 
    
        

    def consec(self, num: int) -> bool:
        if len(self.deque) == self.k : 
            if self.deque[0] == self.value:
                self.count -= 1
            self.deque.popleft() 
        self.deque.append(num)
        if num == self.value :
            self.count += 1
        return self.count == self.k 
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)