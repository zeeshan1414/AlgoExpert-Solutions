def threeLargestNumber(arr):
    first = float('-inf')
    second = float('-inf')
    third = float('-inf')
    for ele in arr:
        if ele > first:
            third = second
            second = first
            first = ele
        elif ele > second:
            third = second
            second = ele
        elif ele > third:
            third = ele
    return [third, second, first]

arr = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(threeLargestNumber(arr))