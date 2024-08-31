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
        max_prob_path = []
        prob = 0
        # need to build dictionary? prob_dict # [connected nodes] : prob
        # path_dict node: [connected]
        prob_dict = {}
        path_dict = {}

        for i, edge_pair in enumerate(edges):
            # add pair: prob
            prob_dict[edge_pair[i][0]] = succProb[i]
            # add node connections
            if path_dict[edge_pair[i][0]] in path_dict:
                path_dict[edge_pair[i][0]].append(edge_pair[1])
            else:
                 path_dict[edge_pair[i][0]] = [(edge_pair[1])]

        print(prob_dict)
        print(path_dict)
    



        return 0 if len(max_prob_path) == 0 else prob


sol = Solution()
print(sol.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start_node = 0, end_node = 2)) 
# 0.25000

print(sol.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start_node = 0, end_node = 2))
# 0.30000