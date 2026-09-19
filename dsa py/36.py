a = list(map(int, (input(), input().split())[1]))
s, ans = [], 0
for i, h in enumerate(a):
    while s and a[s[-1]] < h:
        bottom = a[s.pop()]
        if s: ans += (min(h, a[s[-1]]) - bottom) * (i - s[-1] - 1)
    s.append(i)
print(ans)