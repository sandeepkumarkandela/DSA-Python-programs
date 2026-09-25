from collections import deque
n, k = map(int, input().split())
a = list(map(int, input().split()))
q, res = deque(), []
for i in range(n):
    if q and q[0] <= i - k: q.popleft()
    if a[i] < 0: q.append(i)
    if i >= k - 1: res.append(a[q[0]] if q else 0)
print(*res)