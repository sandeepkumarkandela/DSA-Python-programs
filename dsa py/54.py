a = []
for _ in range(int(input())):
    c = input().split()
    if c[0] == '1':
        a.append(int(c[1]))
    elif c[0] == '2':
        if a:
            a.pop()
    elif c[0] == '3':
        if a:
            print(min(a))