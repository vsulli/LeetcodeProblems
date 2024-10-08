# 2696 - Minimum String Length after Removing Substrings



class Solution:
    def minLength(self, s: str) -> int:
        # can pop 'AB' or 'CD'
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
                continue
            if c == 'B' and stack[-1] == 'A':
                stack.pop()
            elif c == 'D' and stack[-1] == 'C':
                stack.pop()
            else:
                stack.append(c)
        return len(stack)


sol = Solution()

print(sol.minLength(s = "ABFCACDB")) # 2 'FC'

print(sol.minLength(s = "ACBBD")) # 5

