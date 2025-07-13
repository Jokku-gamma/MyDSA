def longest_k(s,k):
    n=len(s)
    if n==0:
        return 0
    i,j=0,0
    if n==k:
        return s
    max_length=0
    uniq_chars=set(s)
    while i<n:
        while j<n:
            window=s[i:j]
            window_chars=set(window)
            if len(window_chars)==k:
                for x in window_chars:
                    if x in uniq_chars:
                        if len(window)>max_length:
                            max_length=len(window)
            j=j+1
        i=i+1 
    return max_length

s1 = "aabbcc"
s2="aabacbebebe"
k1=2
k2=3
print(longest_k(s1,k1))



    
    

            
            
        
'''
s="aaabbccde"
s1=set(s)
m="abcfg"
for x in m:
    if x in s1:
        print(True)
    else:
        print(False)

aaabbbeecde


'''

    
    
