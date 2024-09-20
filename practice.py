s = "babad"
i = 0
m = len(s) // 2
p = len(s) - 1
p-=1
print(s[m::-1]) # m: s   neg step
print(s[m:p+1]) # m:p + 1