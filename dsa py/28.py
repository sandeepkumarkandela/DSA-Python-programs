n = int(input())
a = list(map(int, input().split()))
s, res = [], [-1] * n
for i in range(n - 1, -1, -1):
    while s and s[-1] >= a[i]: s.pop()
    if s: res[i] = s[-1]
    s.append(a[i])
print(*res)