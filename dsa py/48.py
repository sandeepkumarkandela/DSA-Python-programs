from collections import deque
n, k = map(int, input().split())
a = list(map(int, input().split()))
q, res = deque(), []
for i in range(n):
    if q and q[0] <= i - k: q.popleft()
    while q and a[q[-1]] > a[i]: q.pop()
    q.append(i)
    if i >= k - 1: res.append(a[q[0]])
print(*res)