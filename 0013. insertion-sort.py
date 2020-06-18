def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while j>0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

lst = [5,7,3,4,1,3,9]
print(lst)
insertionSort(lst)
print(lst)