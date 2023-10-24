def bubble(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-1-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [2,3,8,6,7]
bubble(arr)
print(arr)
