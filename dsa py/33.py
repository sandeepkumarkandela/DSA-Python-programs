n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
s = list(range(n))

while len(s) > 1:
    a, b = s.pop(), s.pop()
    s.append(b if m[a][b] else a)

c = s[0]
print(c if all(m[i][c] and not m[c][i] for i in range(n) if i != c) else -1)