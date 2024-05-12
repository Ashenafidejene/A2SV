class RecentCounter:

    def __init__(self):
        self.qeue = []

    def ping(self, t: int) -> int:
        self.qeue.append(t)
        while (t-self.qeue[0]>3000):
            self.qeue.pop(0)
        return(len(self.qeue))



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)