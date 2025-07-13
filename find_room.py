def find_room(arr,n):
    return int((n*sum(set(arr))-sum(arr))/(n-1))
    
arr=[1,2,3,6,5,4,4,2,5,3,6,1,6,5,3,2,4,1,2,5,1,4,3,6,8,4,3,1,5,6,2]
n=5
print(find_room(arr,n))