n = int(input())
s = []
for x in map(int, input().split()):
    while s and x < 0 < s[-1]:
        if s[-1] < -x: s.pop(); continue
        elif s[-1] == -x: s.pop()
        break
    else: s.append(x)
print(*s)