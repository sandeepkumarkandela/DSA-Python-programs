from collections import deque
n = int(input())
q = deque(map(int, input().split()))
s, exp = [], 1
while q:
    if q[0] == exp: q.popleft(); exp += 1
    elif s and s[-1] == exp: s.pop(); exp += 1
    else: s.append(q.popleft())
while s and s[-1] == exp:
    s.pop(); exp += 1
print("YES" if exp - 1 == n else "NO")