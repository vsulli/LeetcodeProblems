# Striver's A2Z DSA Course

# Printing Patterns

# Pattern-1: Rectangular Star Pattern

def starPattern(n: int):
    for i in range(n):
        print("*" * n)


'''
starPattern(3)

starPattern(6)
'''

# Pattern-2: Right-Angled Triangle Pattern

def rightTriangle(n: int):
    star_count = 1
    for i in range(n):
        print("*" * star_count)
        star_count += 1

rightTriangle(3)
rightTriangle(6)