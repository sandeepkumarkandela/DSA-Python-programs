from collections import deque
n = int(input())
q = deque(input().split())
q1 = deque(q.popleft() for _ in range(n // 2))
res = []
while q1: res.extend([q1.popleft(), q.popleft()])
print(*res)