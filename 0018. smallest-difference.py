# Brute-Force Approach
def smallestDifference(a, b):
    smallest_pair = []
    smallest = float('inf')
    for i in range(len(a)):
        for j in range(len(b)):
            if abs(a[i] - b[j]) < smallest:
                smallest = abs(a[i] - b[j])
                smallest_pair = [a[i], b[j]]
    return smallest_pair

# O(n*log(n) + m*log(m)) - time complexity


def smallestDiff(a, b):
    a.sort()
    b.sort()
    i = 0
    j = 0
    res = []
    smallest = float('inf')
    while i < len(a) and j < len(b):
        diff = abs(a[i] - b[j])
        if diff < smallest:
            smallest = diff
            res = [a[i], b[j]]
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            return [a[i], b[j]]
    return res


a = [-1, 5, 10, 20, 28, 3]
b = [26, 134, 135, 15, 17]
print(smallestDiff(a, b))
