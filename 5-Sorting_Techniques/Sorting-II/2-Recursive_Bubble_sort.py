def Rbs(arr, n):
    if n == 1:
        return 
    didswap = False
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i+1], arr[i] = arr[i], arr[i+1]
        didswap = True

    if not didswap:
        return 
    Rbs(arr,n-1)
    return arr
arr = [1,9,7,4,2,3,5]
n = len(arr)
print(Rbs(arr,n))