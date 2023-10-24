def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []

    for elem in arr[:-1]:
        if elem <= pivot:
            left.append(elem)
        else:
            right.append(elem)
    return quicksort(left) + [pivot] + quicksort(right)

arr = [2,5,3,4,8,11,21,0,7]

print(quicksort(arr))