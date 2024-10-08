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

        library = {}
        for key, val in pick:
            if key not in library:
                library[key] = {}
            if val not in library[key]:
                library[key][val] = 0
            library[key][val] += 1
        winning_players = 0
        for player in range(n):
            if player in library:
                for count in library[player].values():
                    if count > player:
                        winning_players += 1
                        break
        return winning_players


sol = Solution()


print(sol.winningPlayerCount(n = 4, pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]])) # players 0 & 1 win, 2 & 3 do not

print(sol.winningPlayerCount(n = 5, pick = [[1,1],[1,2],[1,3],[1,4]])) # no one wins game

print(sol.winningPlayerCount(n = 5, pick = [[1,1],[2,4],[2,4],[2,4]])) # player 2 wins game by picking 3 balls with color 4

print(sol.winningPlayerCount(n = 3, pick = [[1, 3], [2, 10]])) # 0