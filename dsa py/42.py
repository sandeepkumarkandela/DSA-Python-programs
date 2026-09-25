class Node:
    def __init__(self, v): self.v, self.n = v, None
h = t = None
for _ in range(int(input())):
    c = input().split()
    if c[0] == '1':
        node = Node(c[1])
        if t: t.n = t = node
        else: h = t = node
    elif c[0] == '2':
        print(h.v)
        h = h.n
        if not h: t = None
    elif c[0] == '3': print(h.v)