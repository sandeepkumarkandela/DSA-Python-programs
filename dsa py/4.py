q = int(input())
main_stack = []
max_stack = []

for _ in range(q):
    query = input().split()
    
    if query[0] == '1':
        x = int(query[1])
        main_stack.append(x)
        if not max_stack:
            max_stack.append(x)
        else:
            current_max = max_stack[-1]
            max_stack.append(max(x, current_max))
            
    elif query[0] == '2':
        main_stack.pop()
        max_stack.pop()
        
    elif query[0] == '3':
        print(main_stack[-1])
        
    elif query[0] == '4':
        print(max_stack[-1])