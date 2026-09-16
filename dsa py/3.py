q = int(input())
stack = []

for _ in range(q):
    query = input().split()
    
    if query[0] == '1':
        x = int(query[1])
        if not stack:
            stack.append((x, x))
        else:
            current_min = stack[-1][1]
            new_min = min(x, current_min)
            stack.append((x, new_min))
            
    elif query[0] == '2':
        stack.pop()
        
    elif query[0] == '3':
        print(stack[-1][0])
        
    elif query[0] == '4':
        print(stack[-1][1])