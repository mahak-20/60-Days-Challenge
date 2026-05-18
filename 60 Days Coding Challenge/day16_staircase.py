import time
def recursive_climb(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return recursive_climb(n-1) + recursive_climb(n-2)


def memo_climb(n, memo={}):
    if n == 1:
        return 1
    if n==2:
        return 2
    if n in memo:
        return memo[n]
    memo[n] = memo_climb(n-1, memo) + memo_climb(n-2, memo)
    return memo[n]

n = int(input("Enter number of stairs: "))

start = time.time()

recursive_climb(n)
end = time.time()

print("Recursive Time: ", end-start)

start = time.time()
memo_climb(n)
end = time.time()
print("Memoized Time: ", end-start)