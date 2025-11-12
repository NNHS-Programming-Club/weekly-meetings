def double(a):
    arr=a
    for i in range(len(arr)):
        n=arr[i]**3
        arr[i]=n
    return(arr)
j=double([10,3,9,27,82,99])
print(j)
