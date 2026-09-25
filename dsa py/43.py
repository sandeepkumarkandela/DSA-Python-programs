q, c = map(int, input().split())
a, head, tail, size = [0] * c, 0, 0, 0
for _ in range(q):
    p = input().split()
    if p[0] == '1':
        if size == c: print("OVERFLOW")
        else: a[tail] = p[1]; tail = (tail + 1) % c; size += 1
    if p[0] == '2':
        if size == 0: print("UNDERFLOW")
        else: print(a[head]); head = (head + 1) % c; size -= 1