
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
        # use a set for the main folder names
        # loop through each string in folder list
        # if the set is empty, just add first one to set and result
        # else read through string of folder
            # if can pass through all but last then it's a subfolder
            # else add to set?
        res = []
        main_folders = set()
        for f in folder:
            if not main_folders:
                main_folders.add(f)
                res.append(f)
            # read through all strings in folder list
            # if all but last letter already in set then don't add
            else:
                # cut string from index 0 to -2 (/c) and if all those other characters DON'T occur in set
                # add full string to set
                folder_slice = f[0:-2]
                if folder_slice not in main_folders:
                    main_folders.add(f)
                    res.append(f)

        return res
        

sol = Solution()

print(sol.removeSubfolders(folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"])) 
# Output: ["/a","/c/d","/c/f"] 


print(sol.removeSubfolders(folder = ["/a","/a/b/c","/a/b/d"]))
# ["/a"]

print(sol.removeSubfolders(folder = ["/a/b/c","/a/b/ca","/a/b/d"]))
# ["/a/b/c","/a/b/ca","/a/b/d"]
