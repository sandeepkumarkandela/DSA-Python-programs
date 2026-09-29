import sys
from collections import deque
lines = sys.stdin.read().splitlines()
if lines:
    c = int(lines[0])
    q = deque()
    for line in lines[1:]:
        if not line: continue
        p = line.split()
        if p[0] == 'put': print("BLOCKED") if len(q) == c else q.append(p[1])
        if p[0] == 'get': print(q.popleft() if q else "NONE")