T = int(input())
for tc in range(1,T+1):
    N, E = map(int,input().split()) # 마지막 연결지점 번호, 도로의 개수
    adjl = [ [] for _ in range(N+1)]

    for _ in range(E):
        s, e, w = map(int,input().split())
        adjl[s].append([e,w])


    # 다익스트라 구현
    # 매 순간 갈 수 있는 가장 가까운 거리를 이동하면서 순회하면, 그것이 해당 노드까지의 최단거리
    start = 0
    end = N

    # 초기화
    cur_min_list = [10**8]*(N+1)  # 해당 index node 까지의 최소 거리
    cur_min_list[start] = 0

    # visited 로 방문 표기
    visited = [0]*(N+1)
    visited[start] = 1

    # 아래 1. 2.를 반복
    # 1. cur_node(최단거리) 를 경로에 포함한 경우, 최소 비용으로 이동할 수 있는 곳들 update
    # 2. 최소 비용으로 이동할 수 있는 곳으로 이동하고, visited 표시


    cur_node  = start
    while visited[N]==0:   # 한 번 방문하면 start에서 해당 노드까지의 최소거리는 바뀌지 않음

        # 1. cur_node에서 최소 비용으로 이동할 수 있는 곳들 update
        for neighbor in adjl[cur_node]:
            next_node, cur_to_next_cost = neighbor

            # next_node로 이동하는 값을 최소 값으로 업데이트
            # 기존 start -> next_node로 가는 거리  >  (기존 start -> cur_node) -> next_node 로 가는 거리
            if cur_min_list[next_node] > cur_min_list[cur_node] + cur_to_next_cost:
                cur_min_list[next_node] = cur_min_list[cur_node] + cur_to_next_cost


        # 2. 최소거리인 곳으로 이동
        min_cost = 10**8
        min_idx = -1
        # 방문하지 않은 모든 노드들 까지의 이동 비용을 탐색
        for node in range(len(cur_min_list)): # 모든 노드
            cost = cur_min_list[node]         # 이동 비용
            if visited[node] == 0 and min_cost > cost:   # 방문하지 않았고, 최소
                min_cost = cost                          # min_cost update
                min_idx = node

        # 최소인 곳 방문
        visited[min_idx] = 1
        cur_node = min_idx


    print(f"#{tc} {cur_min_list[min_idx]}")


