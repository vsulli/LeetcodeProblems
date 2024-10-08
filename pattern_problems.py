# Striver's A2Z DSA Course
# https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/

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

'''
invertedPyramid(3)
invertedPyramid(6)
'''

# Inverted Number Pyramid Same Number
'''
3 3 3  
2 2
1
'''
def invertedNumberPyramidSame(n: int):
    for num in range(n, 0, -1):
        for j in range(num):
            print(num, end = " ")
        print(" ")
'''
invertedNumberPyramidSame(3)
invertedNumberPyramidSame(6)
'''

# Pattern-6: Inverted Numbered Right Pyramid
'''
1 2 3
1 2
1
'''
def invertedNumberPyramid(n: int):
    for i in range(n, 0, -1):
        for j in range(i):
            print(j+1, end = " ")
        print(" ")
'''
invertedNumberPyramid(3)
invertedNumberPyramid(6)
'''

# Pattern-7: Star Pyramid
'''
  *  
 *** 
*****  
'''

def starPyramid(n: int):
    # 1, 3, 5 
    # add 2 to every row
    # spaces will decrease from n-1 to 0?
    stars = 1
    spaces = n - 1
    for i in range(n):
        print(" " * spaces + "*" * stars)
        spaces -= 1
        stars += 2

'''
starPyramid(3)
starPyramid(6)
'''

# Pattern - 8: Inverted Star Pyramid
'''
*****  
 ***
  *
'''
def invertedStarPyramid(n: int):
    # 1, 3, 5 
    # add 2 to every row
    # spaces will decrease from n-1 to 0?
    stars = 1+2*(n-1)
    spaces = 0
    for i in range(n):
        print(" " * spaces + "*" * stars)
        spaces += 1
        stars -= 2

'''
invertedStarPyramid(3)
invertedStarPyramid(6)
'''

# Pattern - 9:Diamond Star Pattern 
'''
  *  
 ***
***** 
*****  
 ***
  *   
'''

def diamondStar(n: int):
    spaces = n - 1
    stars = 1
    for num in range(n):
        print(" " * spaces + "*" * stars)
        stars += 2
        spaces -= 1

    spaces = 0
    stars = 1 + 2*(n - 1)

    for num in range(n, -1, -1):
        print(" " * spaces + "*" * stars)
        stars -= 2
        spaces += 1


'''
diamondStar(3)
diamondStar(6)
'''

# Pattern - 10: Half Diamond Star Pattern
'''
 *  
  **
  ***  
  **
  * 
'''

def halfDiamondStar(n: int):

    for i in range(1, n+1):
        print("*" * i)

    for j in range(n - 1, 0, -1):
        print("*" * j)

'''
halfDiamondStar(3)
halfDiamondStar(6)
'''

# Pattern - 11: Binary Number Triangle Pattern
'''
1
01
101
'''

def binaryTriangle(n: int):
    for row in range(0, n):
        for col in range(0, row + 1):
            if (((row + col) % 2) == 0):
                print("1", end = "")
            else:
                print("0", end = "")
        print("")
    

'''
binaryTriangle(3)
binaryTriangle(6)
'''

#TODO Pattern - 12: Number Crown Pattern
'''
1    1
12  21
123321
'''

def numberCrown(n: int):
    spaces = 2*(n-1)
    for i in range(n):
        for j in range(1,i):
            print(str(j) +  " " + str(j))
        
    
'''
numberCrown(3)
numberCrown(6)
'''
import math
# logarithmic operation Log10(n) + 1
def countDigits(n: int):
    count = int(math.log10(n) + 1)
    return count

print(countDigits(12345))