def binarySearch(arr, key):
    n = len(arr)
    low = 0
    high = n - 1
    while low<=high:
        mid = low+(high-low)//2
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high -= 1
        else:
            low += 1
    return -1

list = [4, 9, 6, 5, 7, 5]
list.sort()
print(list)
key = int( input() )
print(binarySearch(list, key))
