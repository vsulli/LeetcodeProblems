'''
Find Center of Star Graph
Leetcode # 1791
vsulli
27 June 2024

There is an undirected star graph consisting of 
n nodes labeled from 1 to n. A star graph is a 
graph where there is one center node and exactly n - 1 
edges that connect the center node with every other node.

You are given a 2D integer array edges where each 
edges[i] = [ui, vi] indicates that there is an edge 
between the nodes ui and vi. Return the center of the 
given star graph.
'''

class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        # node that is the center will appear in all the subarrays
        # create set of seen
        # when you see another number that is in seen, return that number?
        pass


sol = Solution()

print(sol.findCenter(edges = [[1,2],[2,3],[4,2]])) # 2

print(sol.findCenter(edges = [[1,2],[5,1],[1,3],[1,4]])) # 1

