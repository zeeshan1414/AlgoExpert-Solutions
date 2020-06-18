def bubbleSort(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]

list = [4, 9, 6, 5, 7, 5]
print(list)
bubbleSort(list)
print(list)