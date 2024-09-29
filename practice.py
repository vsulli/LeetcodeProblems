# 729 My Calendar I



class MyCalendar:

    def __init__(self):
        self.schedule = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.schedule:
            if not (end <= s or e <= start):
                return False

        self.schedule.append([start, end])
        return True




# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
print(obj.book(10, 20)) # true
print(obj.book(15, 25)) # false
print(obj.book(20, 30)) # true