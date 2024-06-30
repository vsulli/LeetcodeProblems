'''
Min Stack
Leetcode # 155
vsulli
30 June 2024

Design a stack that supports push, pop, top, and 
retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
'''

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if not self.min or val < self.min:
            self.min = val
        self.stack.insert(0, val)

    def pop(self) -> None:
        # check if popped value is min
        if self.stack[0] == self.min:
            # if it is then set to next lowest
            del self.stack[0]
            if self.stack:
                self.min = min(self.stack)
            else:
                self.min = None
        else:
            del self.stack[0]

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        # how to get min in linear time? 
        # stack is lifo, doesn't guarantee smallest at any index
        # keep track of index when inserting?
        return self.min


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin()) # -3
obj.pop()
print(obj.top()) # return 0
print(obj.getMin()) # return -2
 
