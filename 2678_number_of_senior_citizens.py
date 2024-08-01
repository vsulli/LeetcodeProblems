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
        senior_count = 0

        # Iterate through each passenger's details
        for passenger_info in details:
            # Extract the digits of age
            age_tens = ord(passenger_info[11]) - ord("0")
            age_ones = ord(passenger_info[12]) - ord("0")

            # Calculate the full age
            age = age_tens * 10 + age_ones

            # Check if the passenger is a senior (strictly over 60 years old)
            if age > 60:
                senior_count += 1

        return senior_count

sol = Solution()

print(sol.countSeniors(details = ["7868190130M7522","5303914400F9211","9273338290F4010"])) # 2
print(sol.countSeniors(details = ["1313579440F2036","2921522980M5644"])) # 0