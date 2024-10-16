
'''
Time Based Key-Value Store
Leetcode #981
vsulli
16 October 2024

Design a time-based key-value data structure that can 
store multiple values for the same key at different time 
stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) 
Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a 
value such that set was called previously, with 
timestamp_prev <= timestamp. If there are multiple 
such values, it returns the value associated with the 
largest timestamp_prev. If there are no values, it returns "".
 
'''

class TimeMap:

    def __init__(self):
        self.time_map = {}# key : list of [val, timestamp]


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.time_map.get(key, []) 

        # binary search
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0] # closest we've seen so far
                l = m + 1
            else:
                r = m - 1 # invalid value because we can't go over

        return res


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo", "bar", 1)
param_2 = obj.get("foo", 1) # bar
print(param_2)
param_2 = obj.get("foo", 3) # timestamp 1 -> bar
print(param_2)
obj.set("foo", "bar", 1)


