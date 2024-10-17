# 981 Time Based Key-Value Store

class TimeMap:
    def __init__(self):
        self.store = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
           

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        # retrieve list of values for that key
        values = self.store.get(key, []) # default is empty list
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2

            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return res
        




# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo", "bar", 1)
param_2 = obj.get("foo", 1) # bar
print(param_2)
param_2 = obj.get("foo", 3) # timestamp 1 -> bar
print(param_2)
obj.set("foo", "bar", 1)


