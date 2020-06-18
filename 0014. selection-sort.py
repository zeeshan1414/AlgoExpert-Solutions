def selectionSort(arr):
    n = len(arr)
    currentIdx = 0
    while currentIdx < n-1:
        smallestIdx = currentIdx
        for i in range(currentIdx+1, n):
            if arr[smallestIdx] > arr[i]:
                smallestIdx = i
        arr[currentIdx], arr[smallestIdx] = arr[smallestIdx], arr[currentIdx]
        currentIdx += 1

def cStyle(arr):
    for i in range(0, len(arr)-1):
        smallest = i
        for j in range(i+1, len(arr)):
            if arr[smallest] > arr[j]:
                smallest = j
        arr[smallest], arr[i] = arr[i], arr[smallest]
    return arr

lst = [5,7,3,4,1,3,9]
print(lst)
cStyle(lst)
print(lst)
