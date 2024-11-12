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
*  https://www.youtube.com/watch?v=dOonV4byDEg&ab_channel=ProfoundAcademy

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

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

