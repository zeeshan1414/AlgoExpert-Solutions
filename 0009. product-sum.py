def productSum(arr, multiplier=1):
    sum = 0
    for element in arr:
        if(type(element) is list):
            sum += productSum(element, multiplier+1)
        else:
            sum += element
    return sum*multiplier

arr = [ 5, 2, [7, -1], 3, [6, [-13, 8], 4] ]
sum = productSum(arr)
print(sum)
