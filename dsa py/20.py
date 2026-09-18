n = int(input())
a = list(map(int, input().split()))
s, nxt, idx = [], sorted(a), 0
for x in a:
    s.append(x)
    while s and idx < n and s[-1] == nxt[idx]:
        s.pop()
        idx += 1
print("YES" if not s else "NO")