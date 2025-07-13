def find_pairs(arr,k):
    numbers=set(arr)
    count=0
    for x in arr:
        if x+k in numbers:
            count+=1
    return count

arr=[1,2,3,4,5]
k=3
print(find_pairs(arr,k))