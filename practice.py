# 981 Time Based Key-Value Store

class TimeMap:

    def __init__(self):
        


    def set(self, key: str, value: str, timestamp: int) -> None:
       

    def get(self, key: str, timestamp: int) -> str:

        




# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo", "bar", 1)
param_2 = obj.get("foo", 1) # bar
print(param_2)
param_2 = obj.get("foo", 3) # timestamp 1 -> bar
print(param_2)
obj.set("foo", "bar", 1)


