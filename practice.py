parentheses = []

s = "(abcd)"
# "dcba"
# start(end): index before (to left) where you want to stop 
s = s[0:2] + s[5:1:-1]
print(s)