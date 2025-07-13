def substrings(s):
    res=[]
    n=len(s)
    def backtrack(start):
        if start==n:
            return
        for m in range(start,n):
            res.append(s[start:m+1])
        backtrack(start+1)
    backtrack(0)
    return res

s="aabcd"
print(substrings(s))