N = int(input())
M = int(input())
arrL = [[] for _ in range(M)]
for _ in range(M):
    s, e, c = map(int,input().split())
    arrL[s].append([e,c])

s, e = map(int,input().split())
INF = 0XFFFFFFFFFFFFFF
cost = [INF]*(N+1)

cost[s] = 0
path = []
path.append(s)
for neighbor_cost in arrL[s]:
    n, c = neighbor_cost
    cost[n] = c

min_idx = INF
min_val = INF

while e not in path:

    # 최소인 곳으로 이동
    for node in range(1,N+1):
        if node not in path and cost[node] < min_val:
            min_val = cost[node]
            min_idx = node

    path.append(min_idx)

    # 각 노드로의 이동 최소 비용 update

    # 이동거리 업데이트
    # 기존의 A->B > A->C 기존 + C->B NEW
    for neighbor_cost in arrL[min_idx]:
        n, c = neighbor_cost
        if cost[n] > cost[min_idx] + c:
            cost[n] = cost[min_idx] + c
    print(path)

print(cost[e])
print(len(path))
print(*path)

