'''
Decoded String at Index
Leetcode # 880
vsulli
24 December 2024

You are given an encoded string s. 
To decode the string to a tape, 
the encoded string is read one character 
at a time and the following steps are taken:

If the character read is a letter, 
that letter is written onto the tape.
If the character read is a digit d, 
the entire current tape is repeatedly 
written d - 1 more times in total.
Given an integer k, return the kth 
letter (1-indexed) in the decoded string.

'''

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        # want to return the decoded string at index k (k - 1 index)
        decoded = ""
        for c in s:
            if c.isalpha():
                decoded += c
            else:
                # case where that char is number
                # add to current string - the current string x k - 1
                duplicated =  decoded * (int(c) - 1)
                decoded += duplicated
            # check if k - 1 reached in result and return
            if len(decoded) >= k:
                return decoded[k-1]
        return decoded[k-1]

sol = Solution()

print(sol.decodeAtIndex(s = "leet2code3", k = 10))

print(sol.decodeAtIndex(s = "ha22", k = 5))

print(sol.decodeAtIndex(s = "a2345678999999999999999", k = 1))