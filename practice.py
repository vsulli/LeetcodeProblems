# 729 My Calendar I



class MyCalendar:

    def __init__(self):
        self.schedule = [] 

    def book(self, start: int, end: int) -> bool:
        # if end of new one to book is between start and end, return False
        # if beginning is between start and end, return False
        for i in range(len(self.schedule)):
            # valid if new start is greater than or equal to sched end
            # valid if new end is less than or equal to sched start
            if not(start >= self.schedule[i][1] or end <= self.schedule[i][0]):
                return False
        
        # valid, so add 
        self.schedule.append([start, end])
        return True



# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
print(obj.book(10, 20)) # true
print(obj.book(15, 25)) # false
print(obj.book(20, 30)) # true