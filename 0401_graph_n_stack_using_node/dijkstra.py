def dijkstra(start, end):
    # 1. 시작점에서 다른 노드로 가는 비용을 가지는 배열 D 완성하기
    D = adj[start][:] # 처음에는 시작점과 같음
    D[start] = 0

    # 2. 경로에 포함된 노드들 저장
    U = {start}

    # 3.시작점에서 다른 노드로 가는 비용 확정해나가면 됨
    cur = start
    while cur != end:        # 3.2 전체 노드에 대한 최단 경로 찾으려면  while len(U) < V: # 모든 노드에 대한 최소 경로를 찾아야 함
        # cur 노드를 포함하는 경우에, 갈수 있는 최단 경로 노드
        # 3-1. 초기화
        min_node = -1
        min_value = INF

        # 3-2 이동노드 찾기
        for node in range(V):
            if node not in U and D[node] < min_value:
                min_node = node
                min_value = D[node]

        # 3-3 이동 노드 확정
        U.add(min_node)

        # 3-4 이동한 노드를 기반으로 비용 update
        # 이동한 노드(min_node)를 거쳐서, 다른 노드로 가는 비용 update : D[min_node] + adj[min_node][i]
        for i in range(V):
            if i not in U and D[min_node] + adj[min_node][i] < D[i]: # 새로운 경로 거쳐서, i로 가는 비용 < 기존에 i로 가는 비용
                D[i] = D[min_node] + adj[min_node][i]

        cur = min_node
        print(f"cur is {cur} end is {end}")
        print(D)
    return D


V, E = map(int,input().split())
INF = 0xffffff
adj = [[INF]*V for _ in range(V)]
for _ in range(E):
    s, e, w = map(int,input().split())
    adj[s][e] = w
    adj[e][s] = w

D = dijkstra(0,2)
print(D)

# input
# 6 8
# 0 1 2
# 0 2 4
# 1 2 1
# 1 3 7
# 2 4 3
# 3 4 2
# 3 5 1
# 4 5 5