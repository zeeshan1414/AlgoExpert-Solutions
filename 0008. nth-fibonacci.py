def fib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return fib(n-2) + fib(n-1)

def fibo(n):
    first = 0
    second = 1

    while(n > 1):
        temp = first+second
        first = second
        second = temp
        n -= 1
    return first

def fibDP(n):
    
    arr = [None,0,1]

    for i in range(3, n+1):
        arr.insert(i, arr[i-2] + arr[i-1])
    
    return arr[n]

print(fibo(10))
print(fibDP(10))
