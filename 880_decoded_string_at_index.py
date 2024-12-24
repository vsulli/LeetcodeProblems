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
        # answer will always lie somehwere in the original string
        # k = (k % length of decoded string)
        # reverse solution and stack solution
        decoded_length = 0  # Total length of the decoded string

        for char in s:
            if char.isdigit():
                # If the character is a digit, update the decoded length accordingly
                decoded_length *= int(char)
            else:
                # If the character is a letter, increment the decoded length
                decoded_length += 1

        # Traverse the input string in reverse to decode and find the kth character
        for i in range(len(s) - 1, -1, -1):
            current_char = s[i]

            if current_char.isdigit():
                # If the character is a digit, adjust the length and k accordingly
                decoded_length //= int(current_char)
                k %= decoded_length
            else:
                # If the character is a letter, check if it's the kth character
                if k == 0 or decoded_length == k:
                    return current_char  # Return the kth character as a string

                decoded_length -= 1

        return ""  # Return an empty string if no character is found

sol = Solution()

print(sol.decodeAtIndex(s = "leet2code3", k = 10))

print(sol.decodeAtIndex(s = "ha22", k = 5))

print(sol.decodeAtIndex(s = "a2345678999999999999999", k = 1))