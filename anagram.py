
def find_anagram(words):
    i,j=0,1
    n=len(words)
    result={}
    while i<n:
        word=words[i]
        charset=set(word)
        while j<n:
            CS=set(words[j])
            if CS==charset:
                if word not in result:
                    result[word]=[]
                
                result[word].append(word[j])
            j=j+1
        i=i+1
                
    print(result)


words=["cat","tac","ate","tic","ict"]
print(find_anagram(words))        



