import sys

n, m = map(int, input().split())
arr = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())
    arr[i-1:j] = [k] * (j - (i - 1))

[print(i, end=" ") for i in arr]
