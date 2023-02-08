class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapp = {")":"(","]":"[","}":"{"}
        
        for charr in s:
            if charr in dictn:
                if stack and stack[-1] == mapp[charr]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(charr)
       return True if not stack else False
