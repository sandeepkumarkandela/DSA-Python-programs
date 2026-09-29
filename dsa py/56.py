from collections import deque
n, q_time = map(int, input().split())
b = list(map(int, input().split()))
q = deque((i, b[i]) for i in range(n))
time = 0
while q:
    i, rem = q.popleft()
    if rem <= q_time:
        time += rem
        print(f"{i} {time}")
    else:
        time += q_time
        q.append((i, rem - q_time))