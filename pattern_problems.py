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
    for i in range(0,n):
            for j in range(i+1):
                print('*',end=' ')
            print('')

'''
rightTriangle(3)
rightTriangle(6)
'''

# Pattern-3: Right-Angled Number Pyramid

def numberPyramid(n: int):
    num = 1
    for i in range(n):
        for j in range(i+1):
            print(num, end=' ')
            num += 1
        print('')
        num = 1

'''
numberPyramid(3)
numberPyramid(6)
'''

# Pattern-4: Right-Angled Number Pyramid - II

def numberPyramidII(n: int):
    num = 1 
    for i in range(n):
        for j in range(i+1):
            print(num, end = " ")
        num += 1
        print("")
               
'''
numberPyramidII(3)
numberPyramidII(6)
'''

# Pattern-5: Inverted Right Pyramid
'''
* * *
* * 
*
'''

def invertedPyramid(n: int):
    for num in range(n, 0, -1):
        print("*" * num)

invertedPyramid(3)
invertedPyramid(6)