from collections import deque
n, L = map(int, input().split())
quant = list(map(int, input().split()))
bursts = list(map(int, input().split()))
queues = [deque() for _ in range(L)]
for i, b in enumerate(bursts): queues[0].append((i, b))
time = 0
for lvl in range(L):
    q_time = quant[lvl]
    while queues[lvl]:
        i, rem = queues[lvl].popleft()
        run = min(rem, q_time) if lvl < L - 1 else rem
        time += run
        rem -= run
        if rem == 0: print(f"{i} {time}")
        elif lvl + 1 < L: queues[lvl + 1].append((i, rem))
        else: queues[lvl].append((i, rem))