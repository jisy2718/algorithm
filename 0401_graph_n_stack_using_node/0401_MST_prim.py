
# input
# 7 11    # Node 개수, 간선 개수
# 0 1 32  # 시작, 끝, 가중치
# 0 2 31
# 0 5 60
# 0 6 51
# 1 2 21
# 2 4 46
# 2 6 25
# 3 4 34
# 3 5 18
# 4 5 40
# 4 6 51

INF = 0xfffffff
V, E = map(int,input().split())

adj = [[INF]*V for _ in range(V)]

for e in range(E):
    s, e, w = map(int,input().split())
    adj[s][e] = w
    adj[e][s] = w


# 임의의 시작점 잡고
# 시작점에서 각 노드들로 갈 수 있는 비용 계산하기
# 직접가지 못하면 모든 비용들보다 큰 값 넣어주기
# 그룹을 만들어서... 노드들을 추가할 거고
# 그 그룹에서 다른 노드로 가는 비용을 계산해야 함
# 같은 그룹 내에서 연결된 간선이 바뀌는 경우는 없음! 생각해보면 그럼!

def prim(start):
    group = [0]*V # 1이면 그룹에 포함, 0이면 미포함
    # 시작 정점에서 각 노드들까지 가는데 드는 비용
    weight = adj[start][:]
    weight[start] = 0 # 스스로에게 가는 비용은 0 / 0으로 해줄 필요는 없음
    # 모든 정점이 연결될 때까지 반복하면 됨
    # 최소 비용으로 연결할 수 있는 노드 고르기
    print(start, 0)
    for _ in range(V-1): # V-1 개 간선 찾으면 됨
        # 최소비용 계산 / 목표는 min_V 와 min_idx 찾는 것
        min_V = INF
        min_idx = start # 그룹에 포함된 아무노드로 초기화

        # weight 배열(각 노드까지 방문하는 비용) 검사하면서
        # 방문하지 않았고, 방문 비용이 최소인 노드 찾음
        for i in range(V):
            # 가는 비용 최소이고, 방문하지 않았으면
            if weight[i] < min_V and not group[i]:
                min_V = weight[i]
                min_idx = i
        # 반복문이 끝나면 min_V : 최소 방문 비용, min_idx에 방문할 노드 저장되어 있음
        group[min_idx] = 1 # group에 포함시킴
        print(min_idx, min_V)

        # min_idx가 group에 update 되었으므로
        # 1. min_idx에서 새로운 노드로 갈 수 있는지
        # 2. min_idx 반영해, 기존 노드들과의 비용 다시 계산
        for i in range(V):
            if weight[i] > adj[min_idx][i] and not group[i]:
                weight[i] = adj[min_idx][i]




prim(0)
# 7 11
# 0 1 32
# 0 2 31
# 0 5 60
# 0 6 51
# 1 2 21
# 2 4 46
# 2 6 25
# 3 4 34
# 3 5 18
# 4 5 40
# 4 6 51