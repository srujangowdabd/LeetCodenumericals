class Solution(object):
    def canRemoveAll(self, types, colors, groupSize):
        stack = []
        for t,c in zip (types , colors):
            if stack and stack[-1][0] == t and stack [-1][1] == c:
                stack[-1][2] += 1
            else:
                stack.append([t,c,1])
            if stack[-1][2] == groupSize[t]:
             stack.pop()
                
                
        return len(stack)==0      
             
