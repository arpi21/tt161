def shell(arr):
    gap = len(arr)//2

    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i

            while j >= gap and arr[j-gap]> temp:
                arr[j] = arr[j-gap]
                j-=gap
            arr[j] = temp
        gap //=2

arr = [1,4,67,2,3,56]
shell(arr)
print(arr)

