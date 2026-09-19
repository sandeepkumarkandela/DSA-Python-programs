n = int(input())
p = list(map(int, input().split()))
s, res = [], []
for i in range(n):
    while s and p[s[-1]] <= p[i]: s.pop()
    res.append(i + 1 if not s else i - s[-1])
    s.append(i)
print(*res)