def count_zero(N):
    count=0
    x=1
    for x in range(N+1):
        x=str(x)
        if '0' in x:
            count+=1
    return count
print(count_zero(105))
