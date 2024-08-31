'''
Path with Maximum Probability
Leetcode # 1514
vsulli
31 August 2024

You are given an undirected weighted 
graph of n nodes (0-indexed), represented 
by an edge list where edges[i] = [a, b] is 
an undirected edge connecting the nodes a 
and b with a probability of success of 
traversing that edge succProb[i].

Given two nodes start and end, find the 
path with the maximum probability of success 
to go from start to end and return its success 
probability.

If there is no path from start to end, return 0. 
Your answer will be accepted if it differs from 
the correct answer by at most 1e-5.
'''

from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        pass

sol = Solution()
print(sol.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2)) 
# 0.25000

print(sol.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2))
# 0.30000