# Leetcode Problems
These are my submissions to leetcode, including initial attempts. After attempting each question I have found either an optimized solution online or a solution suggested by Neetcode to study and learn from. 

Rather than focusing on solving as many problems as possible, my goal is to understand all of the data structures and algorithms behind each problem and learn them by concept. This will enable me to apply what I learn to unseen problems in the future to solve them more efficiently. 


# Resources

**Websites**

[Leetcode](https://leetcode.com/problemset/)

[Neetcode](https://neetcode.io/roadmap)

**Books**

Cracking the Coding Interview


# Data Structures
1. Linked Lists
2. Trees, Tries, Graphs
3. Stacks & Queues
4. Heaps
5. Vectors / ArrayLists
6. Hash Tables


# Algorithms
1. Breadth-First Search
2. Depth-First Search
3. Binary Search 
4. Merge Sort
5. Quick Sort
6. Topological Sort
7. Bucket Sort
8. Dijkstra's (Shortest Path)
9. Union-Find 
10. A* Search
11. Kruskal's (Minimum Spanning Forest of Graph)
12. Prim's (Minimum Spanning Tree for Weighted Undirected Graph)
13. String-Searching Algorithms
14. Floyd's Algorithm (Shortest Path in a Directed Weighted Graph)
15. Floyd's Cycle Finding Algorithm / Hare-Tortoise Algorithm


# Concepts
1. Bit Manipulation
2. Memory (Stack vs. Heap)
3. Recursion
4. Dynamic Programming
5. Big O Time & Space
6. Backtracking
7. Sliding Window
8. Two Pointers
9. Prefix Sum
10. Binary Search (Tree)
11. Quickselect
12. Binary Manipulation
13. Finding Middle of List with Fast & Slow Pointers


## Big O Notation
3 Rules for Calculating It
- always calculate the worst-case scenario
- avoid including constant terms
- avoid lower values

## Arrays & Hashing

### Arrays & Hashing - Leetcode Questions
1929 - Concatenation of Array
217 - Contains Duplicate
1 - Two Sum
146 - LRU Cache
303 - Range Sum Query - Immutable
304 - Randge Sum Query 2D - Immutable
724 - Find Pivot Index
238 - Product of Array Except Self
560 - Subarray Sum Equals K
242 - Valid Anagram
49 - Group Anagrams
347 - Top K Frequent Elements
(premium) 271 - Encode and Decode Strings
36 - Valid Sudoku
128 - Longest Consecutive Sequence



## Two Pointers

given a sorted array you can reduce it down to O(n) instead of O(n^2)
ex) Two Sum
left and right pointers
if sum is too low, increment left pointer
if sum is too high, increment right pointer
if pointers meet then there is no solution

When to use:
* finding which numbers add up to a target
* finding items that sum to 0 in a given array
* finding max water between two walls


##  Sliding Window
*  sliding window technique video lesson
*  [Sliding Window Technique](https://www.youtube.com/watch?v=dOonV4byDEg&ab_channel=ProfoundAcademy)

Fixed Window Example)
arr = [8, 3, -2, 4, 5, -1, 0, 5, 3, 9, -6], k = 5 # output: 18
Maximum Sum Subarray of Size K 

currSum = maxSum = sum(arr[:k]) # calculates intitial sum of size k
for r in range(k, len(arr)) # loops through starting at next index
    currSum += arr[r] - arr[r - k] # adds on rightmost index, subtracts off leftmost
    maxSum = max(maxSum, currSum)
return maxSum


Dynamic Window Example)
Longest Subarray with Sum < S 
s = 15
arr = [4, 5, 2, 0, 1, 8, 12, 3, 6, 9]

* two pointers, one before the start and the other at the start of the current window (0)
* *at each step, adjust the right by one, move the left to make sure sum of current window doesn't exceed threshold

from typing import List

*  find longest subarray that has a sum less than "s"
class Solution:
    def longestSubarraySum(self, arr: List[int], s: int) -> int:
        # initialize left pointer, current sum, and max length
        l, currSum, maxLen = -1, 0, 0
        for r in range(len(arr)):
            currSum += arr[r]
            while currSum >= s: # adjust subarray while sum greater than s
                l += 1
                currSum -= arr[l]
            # update max length
            maxLen = max(maxLen, r - l) # take right index minus left index
        return maxLen


## Binary Tree

* hierarchical structure
* one node is marked as the "root"
* every other node has a parent node
* each node can have at most 2 children (left child less than parent, right child greater than parent)

Advantages of Binary Tree: searching, inserting, deleting, sorted order

Disadvantages of Binary Tree: unbalanced trees are inefficient, 
worst case O(n) for searching and insertion, extra memory for pointers to children, inefficient for large datasets, limited functions that work well with this data structure

Common Operations: insertion, deletion, inorder traversal, preorder traversal, postorder traversal, level order traversal, max depth/height of tree, enumeration of binary tree, bfs for a bst, dfs for a bst

Enumeration of a binary tree: the number of distinct binary trees formed from a given number of nodes of a binary tree

Given N nodes, we may find the number of different labelled binary Trees

C(N) = n! * ( (2n!) / (n+1)! * n! ) )

Node Class for a Binary Search Tree

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```
### Binary Search Tree - Leetcode Problems
701 - Insert into a Binary Search Tree
450 - Delete Node in a BST
94 - Binary Tree Inorder Traversal
144 - Binary Tree Preorder Traversal
145 - Binary Tree Postorder Traversal
105 - Construct Binary Tree from Preorder and Inorder Traversal
102** - Binary Tree Level Order Traversal
199 - Binary Tree Right Side View
173 - Binary Search Tree Iterator
226 - Invert Binary Tree
104 - Maximum Depth of Binary Tree
543 - Diameter of Binary Tree
110 - Balanced Binary Tree
100 - Same Tree
572 - Subtree of Another Tree
235 - Lowest Common Ancestor of a Binary Search Tree
1448 - Count Good Nodes in Binary Tree
98 - Validate Binary Search Tree
230 - Kth Smallest Element in a BST
124 - Binary Tree Maximum Path Sum
297 - Serialize and Deserialize Binary Tree

# Notes
**Lambda Functions**
[Lambda Function - Python](https://www.w3schools.com/python/python_lambda.asp)
[Lambda Functions Explained](https://www.youtube.com/watch?v=HQNiSfb795A&ab_channel=TechWithTim)

Syntax: 
lambda arguments : expression


add_1 = lambda x, y: x + y

result = add_1(1, 7)
print(result) # 8

* Lambda functions can accept any number of parameters & they can return any valid python expression


```python
def add_1(x, y):
    return x + y

add_1 = lambda x, y: x + y
```

* both of these do the same thing

```python
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x:x % 2 == 0, my_numbers))
print(evens)
```

* filtering of an iterable object
* will only keep values that return True

```python
values = [(1, 'b', "hello"), (2, 'a', "world"), (3, 'c', "ok")]
sorted_values = sorted(values, key=lambda x: x[1], reverse=True) 
print(list(sorted_values))
```

* sorting function
* this is sorted based on the 2nd value (index 1) 
* [(2, 'a', 'world'), (1, 'b', 'hello'), (3, 'c', 'ok')]
* reverse = True will sort in descending order
