def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1)+fib(n-2)

# print(fib(50))

def fib_memo(n, memo={0:0, 1:1}):
    if n not in memo:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

print(fib_memo(100))