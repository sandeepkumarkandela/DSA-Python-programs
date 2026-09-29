from collections import deque
q = deque()
for _ in range(int(input())):
    t = int(input())
    q.append(t)
    while q[0] < t - 3000: q.popleft()
    print(len(q))