# binary search using recursion
# returns the index of the found value, returns -1 if not found
def bsearch(arr, value , low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            return bsearch(arr, value, mid +1, high)
        else:
            return bsearch(arr, value, low, mid - 1)

    return -1


arr = [1,2,3,4,5]
print(bsearch(arr, 8, 0, len(arr)-1))


