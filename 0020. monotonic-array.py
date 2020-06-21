def isMonotonic(arr):
    isUp = True
    isDown = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            isDown = False
        elif arr[i] < arr[i-1]:
            isUp = False

    return isUp or isDown


if __name__ == "__main__":
    arr0 = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
    arr1 = [1, 1, 1, 2, 3, 4, 3, 4, 5]
    print(isMonotonic(arr1))
