# O(N) - time complexity
def moveToEnd(arr, k):
    i = 0
    j = len(arr) - 1

    while i < j:
        if arr[i] == k:
            if arr[i] != arr[j]:  #dont swap if equal
                print(arr[i], arr[j])
                arr[i], arr[j] = arr[j], arr[i]  #swap
            j -= 1
        else:
            i += 1
    return arr


if __name__ == "__main__":
    arr0 = [2, 1, 2, 2, 2, 3, 4, 2]
    arr1 = [3, 5, 0, 0, 4]
    arr2 = [0, 0, 0, 4]
    arr3 = [4, 2, 1, 3, 2, 2, 2, 2]
    # arr.sort()
    # print(arr)
    print(moveToEnd(arr0, 2))
    # print(moveToEnd(arr1, 0))
    # print(moveToEnd(arr2, 0))
    # print(moveToEnd(arr3, 2))
