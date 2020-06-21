# O(n)
def spiralTraverse(arr):
    res = []
    startRow, endRow = 0, len(arr) - 1
    startCol, endCol = 0, len(arr[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol+1):
            res.append(arr[startRow][col])

        for row in range(startRow+1, endRow + 1):
            res.append(arr[row][endCol])

        for col in reversed(range(startCol, endCol)):
            res.append(arr[endRow][col])

        for row in reversed(range(startRow+1, endRow)):
            res.append(arr[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return res


if __name__ == "__main__":
    arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            print(arr[i][j], end=' ')
        print()
    print(spiralTraverse(arr))
