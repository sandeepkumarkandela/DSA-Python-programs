n = int(input())
s = list(map(int, input().split()))
t = []
while s:
    tmp = s.pop()
    while t and t[-1] < tmp: s.append(t.pop())
    t.append(tmp)
while t: print(t.pop(), end=" ")
print()