class Solution:
    def __init__(self,s):
        self.s=s
    def lengthoflongestSubstring(self,s):
        n=len(s)
        if n==0:
            return 0
        max_length=0
        char_Set=set()
        left=0
        for right in range(n):
            while s[right] in char_Set:
                char_Set.remove(s[left])
                left+=1
            char_Set.add(s[right])
            max_length=max(max_length,right-left+1)
        return char_Set,max_length
s="aaaaaa"
obj=Solution(s)
print(obj.lengthoflongestSubstring(s))