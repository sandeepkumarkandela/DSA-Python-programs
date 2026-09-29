c = int(input())
q_num=int(input())
cache = []
for _ in range(q_num):
    query = input().split()[1]
    if u in cache: cache.remove(u)
    elif len(cache) == c: cache.pop(0)
    cache.append(u)
    print(*(cache[::-1]))