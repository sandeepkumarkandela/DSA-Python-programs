# 1. Read the number of queries
q = int(input()) 

# 2. Create our empty stack
stack = []       

# 3. Loop exactly 'q' times
for _ in range(q):
    # Read the query line and split it into a list of words/numbers
    query = input().split() 
    
    if query[0] == '1':
        # Push: query looks like ['1', '10']
        x = int(query[1])
        stack.append(x)
        
    elif query[0] == '2':
        # Pop: query looks like ['2']
        stack.pop()
        
    elif query[0] == '3':
        # Top: query looks like ['3']
        print(stack[-1])