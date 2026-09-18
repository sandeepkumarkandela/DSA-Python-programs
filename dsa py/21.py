s = []
for _ in range(int(input())):
    p = input().split()
    if p[0] == '1': s.append(p[1])
    if p[0] == '2': s.pop()
    if p[0] == '3':
        k = int(p[1])
        print(s[len(s) - 1 - k] if 0 <= k < len(s) else "INVALID")