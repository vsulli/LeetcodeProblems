# Daily Practice Sheet for use with ANKI

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = []
        groups = {}
        # use sorted word as key, add to list any words that match
        for word in strs:
            if str(sorted(word)) in groups:
                groups[str(sorted(word))].append(word)
            else:
                groups[str(sorted(word))] = [word]
        
        for key in groups:
            ans.append(groups.get(key))

        return ans

sol = Solution()

print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))

print(sol.groupAnagrams(strs = [""]))

print(sol.groupAnagrams(strs = ["a"]))