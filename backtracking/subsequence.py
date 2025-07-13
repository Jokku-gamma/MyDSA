def subsequence(s):
    res=[]
    n=len(s)
    def backtrack(start,curr):
        if start==n:
            res.append(curr)
            return
        backtrack(start+1,curr)
        backtrack(start+1,curr+s[start])
    backtrack(0,"")
    res.sort(key=lambda x:(len(x),x))
    return res

s="abc"
print(subsequence(s))