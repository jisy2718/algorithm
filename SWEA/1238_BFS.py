# graph에서 가장 마지막에 탐색된 노드들 중, 가장 큰 값의 노드를 구하는 문제이다.
#
import sys
sys.stdin = open('1238_input.txt')


T = 10
for tc in range(1,T+1):
    E, s = map(int,input().split())
    Edges = list(map(int,input().split()))

    max_num = 0
    for num in Edges:
        if num > max_num:
            max_num = num

    # 빈 graph 생성
    graph = [[0]*(1+max_num) for _ in range(1+max_num)] # 1 ~ max_num idx 이용
    visited = [False]*(1+max_num)
    # graph 노드 연결
    for i in range(0,len(Edges),2):
        # 앞 노드에서 뒷 노드로 연결
        graph[Edges[i]][Edges[i+1]] = 1 # 행, 열 순

    # BFS로 탐색
    queue = [[s,1]] # s에서 시작
    visited[s] = True
    last = 0
    last_num = 0
    while queue:
        c_node, c_dist = queue.pop()

        for i in range(1,max_num+1):
            if graph[c_node][i] == 1 and visited[i]==False:
                visited[i] = True
                queue.append([i,c_dist + 1])

        if last < c_dist:
            last = c_dist
            last_num = c_node
        elif last == c_dist and last_num < c_node: # 기존 마지막 수보다, 더 크면 update
            last_num = c_node
        print(f'cur last {last} and last_num : {last_num}')
    print(f'#{tc} {last_num}')





