from collections import Counter
def find_ballons(string):
    count=0
    freq1=Counter(string)
    target="balloon"
    freq2=Counter(target)
    org=Counter()
    for x,y in freq1.items():
        if x not in freq2:
            continue
        else:
            org[x]=y
    diff=org-freq2
    print(diff)
    while diff is True:
        count+=1
        diff=diff-freq2
    return count

    

                    
string="loonbalxballpoon"
print(find_ballons(string))
    
            
        

        

