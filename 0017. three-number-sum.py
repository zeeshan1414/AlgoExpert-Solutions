# O(n^3) - time complexity
def threeSums(arr, key):
    res = []
    n = len(arr)
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if(arr[i] + arr[j] + arr[k] == key):
                    res.append([arr[i], arr[j], arr[k]])
    return res

# (n^2) - time complexity


def threeSumsWithTwoLoops(arr, key):
    res = []
    arr.sort()
    n = len(arr)
    for i in range(0, n-2):
        j = i + 1
        k = n - 1
        while j < k:
            currSum = arr[i] + arr[j] + arr[k]
            if currSum == key:
                res.append([arr[i], arr[j], arr[k]])
                j += 1
                k -= 1
            elif currSum < key:
                j += 1
            else:
                k -= 1
    return res


ar = [12, 3, 1, 2, -6, 5, -8, 6]
target = 5
print("arr =", ar)
print("target =", target)
print(threeSumsWithTwoLoops(ar, target))
