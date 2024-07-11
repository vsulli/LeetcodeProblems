parentheses = []

s = "(abcd)"
# "dcba"
# start: index before where you want to stop 
s = s[0:2] + s[:1:-1]
print(s)