def insertion(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i-1
        while j >= 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = current
    return arr


arr = [1, 5, 2, 4, 8]
print(insertion(arr))
