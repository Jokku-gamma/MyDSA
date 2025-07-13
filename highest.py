def highest(arrays,n):
    A=[0]*n
    for arr in arrays:
        x,y,z=arr[0],arr[1],arr[2]
        for m in range(x,y):
            A[m]+=z
    return max(A)
arrays=[[1,3,5], [2,4,7], [2,4,3]]
n=10
print(highest(arrays,n))