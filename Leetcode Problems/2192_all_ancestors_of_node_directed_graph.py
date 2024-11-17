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
        ans = [[] for _ in range(n)]
        directChild = [[] for _ in range(n)]
        for e in edges:
            directChild[e[0]].append(e[1])
        for i in range(n):
            self.dfs(i, i, ans, directChild)
        return ans

    def dfs(self, x: int, curr: int, ans: list[list[int]], directChild: list[list[int]]) -> None:
        for ch in directChild[curr]:
            if not ans[ch] or ans[ch][-1] != x:
                ans[ch].append(x)
                self.dfs(x, ch, ans, directChild)

        # 0 -> 3, 4
        # 1 -> 3
        # 2 -> 4, 7
        # 3 -> 5, 6, 7
        # 4 -> 6

sol = Solution()

print(sol.getAncestors(n = 8, edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))