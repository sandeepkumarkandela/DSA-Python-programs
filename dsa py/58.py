from collections import deque
k = int(input())
stream = list(map(int, input().split()))
q, total = deque(), 0
for val in stream[1:]:
    q.append(val)
    total += val
    if len(q) > k: total -= q.popleft()
    print(f"{total / len(q):.2f}")