
'''
Remove Sub-Folders from the Filesystem
Leetcode #1233
vsulli
25 October 2024

Given a list of folders folder, return the folders 
after removing all sub-folders in those folders. 
You may return the answer in any order.

If a folder[i] is located within another folder[j],
it is called a sub-folder of it. A sub-folder of 
folder[j] must start with folder[j], followed by a 
"/". For example, "/a/b" is a sub-folder of "/a",
 but "/b" is not a sub-folder of "/a/b/c".

The format of a path is one or more concatenated 
strings of the form: '/' followed by one or more 
lowercase English letters.

For example, "/leetcode" and "/leetcode/problems" 
are valid paths while an empty string and "/" are not.
'''

from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()

        folder_set = set()
        for f in folder:
            n = len(f)
            exist = False
            for i, c in enumerate(f):
                if c == "/":
                    if f[:i] in folder_set: # check if everything before last / is in set ignore
                        exist = True
                        break
            if not exist:
                folder_set.add(f)
        return list(folder_set)

sol = Solution()

print(sol.removeSubfolders(folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"])) 
# Output: ["/a","/c/d","/c/f"] 


print(sol.removeSubfolders(folder = ["/a","/a/b/c","/a/b/d"]))
# ["/a"]

print(sol.removeSubfolders(folder = ["/a/b/c","/a/b/ca","/a/b/d"]))
# ["/a/b/c","/a/b/ca","/a/b/d"]
