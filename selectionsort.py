def selection(arr):
    for i in range(len(arr)):
        min = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]


arr = [1,4,2,11,8,5]
selection(arr)
print(arr)
