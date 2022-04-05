# prim 알고리즘
# 1. 0번노드에서 시작하기로 결정

# 2. 현재 선택된 노드들에서 다른 노드들로 이동할 때 드는 비용 계산

# 3. 비용이 최소인 다른 노드 선택

# 4. 선택한 노드 반영하여, 최소 연결비용 update
def prim(start):
    mst = []
    result = 0
    used = {start}
    # 이동 비용 초기화
    cost = adj[start][:]


    while len(used) < V+1:  # while문이 끝까지 V번 실행되면 됨. 현재 used = 1에서 1번실행됨

        # 이동하는 데 드는 비용 update
        for used_node in used: # 사용된 노드들에서
            for v in range(1,V+1):  # 사용되지 않은 다른 노드들 까지의 비용 update
                if v not in used:
                    # 기존 경로의 cost 보다 새로운 경로의 코스트가 더 싸면 update
                    if cost[v] > adj[used_node][v]:
                        cost[v] = adj[used_node][v]

        # 최소비용 노드 찾기
        min_node = -1
        min_cost = 1000*10
        for v in range(V+1):
            if v not in used:
                if cost[v] < min_cost:
                    min_cost = cost[v]
                    min_node = v

        # 최소비용 노드 찾았으니 선택
        used.add(min_node)
        result += min_cost

    return result

T = int(input())
for tc in range(1,T+1):
    # 1. input
    V, E = map(int,input().split())
    adj = [[1000*10]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        s, e, w = map(int,input().split())
        adj[s][e] = w
        adj[e][s] = w


    result = prim(0)
    print(f"#{tc} {result}")