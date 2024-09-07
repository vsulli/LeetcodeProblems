'''
Find the Number of Winning Players
Leetcode # 3238
vsulli
7 September 2024

You are given an integer n representing the 
number of players in a game and a 2D array 
pick where pick[i] = [xi, yi] represents that 
the player xi picked a ball of color yi.

Player i wins the game if they pick strictly 
more than i balls of the same color. In other words,

Player 0 wins if they pick any ball.
Player 1 wins if they pick at least two balls 
of the same color.
...
Player i wins if they pick at leasti + 1 balls 
of the same color.
Return the number of players who win the game.

Note that multiple players can win the game.
'''

from typing import List


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        # n is number of players
        # array has picks player: color 
        # a player wins if they pick one more number of balls of same color than their number

        # need to loop through list of picks
        # keep dictionary of player number to picks and their count for each number
        # player # 0: [] list of picks initialized as size 10?

        # are picks always going to be in order?

        winners = 0
        pick_counts = {} 
        for p in pick:
            if p[0] in pick_counts:
                # update count of color at that index
                pick_counts[p[0]][p[1]] += 1
            else:
                # add player to dict and initialize picks array to size 10
                pick_counts[p[0]] = [0] * 10
                pick_counts[p[0]][p[1]] = 1
        
        # print(pick_counts)

        # now need to loop through players in dictionary
        for player in pick_counts:
            max = sorted(pick_counts.get(player), reverse=True)
            if max[0] > player:
                winners += 1
            # print(max[0])
        return winners


sol = Solution()


print(sol.winningPlayerCount(n = 4, pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]])) # players 0 & 1 win, 2 & 3 do not

print(sol.winningPlayerCount(n = 5, pick = [[1,1],[1,2],[1,3],[1,4]])) # no one wins game

print(sol.winningPlayerCount(n = 5, pick = [[1,1],[2,4],[2,4],[2,4]])) # player 2 wins game by picking 3 balls with color 4
