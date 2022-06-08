N, M = map(int,input().split())

make_set = [x for x in range(N+1)]

def find_root(a):
    if make_set[a] == a:
        return a

    else:
        return find_root(make_set[a])

def union(a,b):
    root_a = find_root(a)
    root_b = find_root(b)

    make_set[root_b] = root_a


for _ in range(M):
    s, e = map(int,input().split())

    union(s,e)

result = 0
for i in range(1,N+1): # i == 0인 경우 제외
    if make_set[i] == i:
        result += 1

print(result)
