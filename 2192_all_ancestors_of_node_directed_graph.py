'''
All Ancestors of a Node in a Directed Acyclic Graph
Leetcode # 2192
vsulli
29 June 2024

You are given a positive integer n representing 
the number of nodes of a Directed Acyclic Graph 
(DAG). The nodes are numbered from 0 to n - 1 
(inclusive).

You are also given a 2D integer array edges, 
where edges[i] = [fromi, toi] denotes that there 
is a unidirectional edge from fromi to toi in 
the graph.

Return a list answer, where answer[i] is the 
list of ancestors of the ith node, sorted in 
ascending order.

A node u is an ancestor of another node v 
if u can reach v via a set of edges.
'''

class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        pass
        answer = []
        # create hashmap?
        # lowest number key will store top nodes?
        nodes = {}
        # 0, 1, 2 as top nodes
        for i in range(len(edges)):
            if edges[i][0] in nodes:
                nodes[edges[i][0]].append(edges[i][1])
            else:
                nodes[edges[i][0]] = [edges[i][1]]

        # loop through keys of hashmap
        # while can still find value in hashmap, append that key to its list
        for i in range(len(nodes)):
            print(i)
            try:
            # get all keys from a value
                keys = [k for k,v in nodes.items() if v == i]
                print(keys)
                answer.append(keys)
            except:
                print("No ancestors")
                answer.append([])
        # print(nodes)
        return answer

        # 0 -> 3, 4
        # 1 -> 3
        # 2 -> 4, 7
        # 3 -> 5, 6, 7
        # 4 -> 6

        # loop through hashmap getting key
        # if key doesn't occur anywhere else then it doesn't have ancestors
        # if it does occur elsewhere, then sort those keys in ascending order
        # must recursively look for those ancestors

        

sol = Solution()

print(sol.getAncestors(n = 8, edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))