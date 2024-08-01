'''
Number of Senior Citizens
Leetcode # 2678
vsulli
31 July 2024

You are given a 0-indexed array of strings details. 
Each element of details provides information about a 
given passenger compressed into a string of length 15. 
The system is such that:

The first ten characters consist of the phone number of passengers.
The next character denotes the gender of the person.
The following two characters are used to indicate the age of the person.
The last two characters determine the seat allotted to that person.
Return the number of passengers who are strictly more than 60 years old.
'''

class Solution:
    def countSeniors(self, details: list[str]) -> int:
        count = 0
        # need to loop through all details
        # slice from end of list-3:-5
        # if that slice > 60 increase count

        for i in details:
            if int(i[11:13]) > 60:
                count += 1

        return count

sol = Solution()

print(sol.countSeniors(details = ["7868190130M7522","5303914400F9211","9273338290F4010"])) # 2
print(sol.countSeniors(details = ["1313579440F2036","2921522980M5644"])) # 0