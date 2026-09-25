from collections import deque
n, k = map(int, input().split())
q = deque(input().split())
s = []
for _ in range(k): s.append(q.popleft())
while s: q.append(s.pop())
for _ in range(n - k): q.append(q.popleft())
print(*q)