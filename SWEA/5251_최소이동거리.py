T = int(input())
for tc in range(1,T+1):
    N, E = map(int,input().split()) # 마지막 연결지점 번호, 도로의 개수
    adjl = [ [] for _ in range(N+1)]

    for _ in range(E):
        s, e, w = map(int,input().split())
        adjl[s].append([e,w])

    # print(adjl)

    # 다익스트라 구현
    start = 0
    end = N
    cur_min_list = [10**8]*(N+1)
    cur_min_list[start] = 0
    selected = {start}
    visited = [0]*(N+1)
    visited[0] = 1
    # 첫 위치에서, 최소 비용으로 이동할 수 있는 곳들 update

    # 최소 비용으로 이동할 수 있는 곳으로 이동하고, selected 에 넣기

    # 현재 새로 선택한 노드에서 이동할 수 있는 최소 비용 update 후 최소 비용인 곳으로 이동
    cur_node  = start
    while visited[N]==0:
        for neighbor in adjl[cur_node]:
            next_node, cur_to_next_cost = neighbor
            # print(f"cur node : {cur_node}, cur_min_list[next_node]:{cur_min_list[next_node]}, next_node : {next_node}, cur_to_next_cost : {cur_to_next_cost}")
            # next_node로 이동하는 값을 최소 값으로 업데이트
            if cur_min_list[next_node] > cur_min_list[cur_node] + cur_to_next_cost:
                cur_min_list[next_node] = cur_min_list[cur_node] + cur_to_next_cost
        # print(cur_min_list)

        min_cost = 10**8
        min_idx = 0
        for node in range(len(cur_min_list)):
            cost = cur_min_list[node]
            if visited[node] == False and min_cost > cost:
                min_cost = cost
                min_idx = node

        # 최소인 곳 방문
        # print(f"min_idx : {min_idx}, cur_min_list : {cur_min_list}")
        visited[min_idx] = 1
        cur_node = min_idx


    print(f"#{tc} {cur_min_list[min_idx]}")


