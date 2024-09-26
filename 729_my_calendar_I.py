'''
My Calendar I
Leetcode # 729
vsulli
26 September 2024

You are implementing a program to use as 
your calendar. We can add a new event if 
adding the event will not cause a double booking.

A double booking happens when two events 
have some non-empty intersection (i.e., 
some moment is common to both events.).

The event can be represented as a pair of 
integers start and end that represents a 
booking on the half-open interval [start, end), 
the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true 
if the event can be added to the calendar successfully 
without causing a double booking. Otherwise, return 
false and do not add the event to the calendar.
'''

class MyCalendar:

    def __init__(self):
        self.schedule = {} # use a hashset? start:end

    def book(self, start: int, end: int) -> bool:
        # as long as the start you want to add is equal to or greater than all the ends
        # then you can add it?
        # also cannot match a start that's already in schedule
        for k in self.schedule:
            if start > k and start < self.schedule.get(k):
                return False
        
        # add new booking
        # return true
        self.schedule[start] = end
        return True



# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
print(obj.book(10, 20)) # true
print(obj.book(15, 25)) # false
print(obj.book(20, 30)) # true