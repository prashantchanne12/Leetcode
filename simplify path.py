'''
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.
'''


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        stack = []
        current = ''

        # path + '/' for '/a/.."
        # path = '/a/../'

        for p in path + '/':

            if p == '/':
                '''
                1) ../  -> pop from stack
                2) abc/ -> add abc to stack
                3) /, // -> ignore
                4) ./   -> ignore
                '''

                if current == '..':
                    if stack:
                        stack.pop()

                else:

                    if current != '' and current != '.':
                        stack.append(current)

                current = ''

            else:

                current += p  # . .. a, b, etc.

        return '/' + '/'.join(stack)

# Solution 2
class Solution:
    def simplifyPath(self, path: str) -> str:
        splitted_path = path.split("/")
        stack = []
        res = ""
        
        for string in splitted_path:
            if string == "" or string == ".":
                continue
            
            if string == "..":
                if stack:
                    stack.pop()
                continue
            
            stack.append(string)
        
        return '/' + '/'.join(stack) 


