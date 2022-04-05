
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    graph = [[0]*(N+1) for _ in range(N+1)]  # 1~N 가지 이용

    graphL  = [[]*(N+1) for _ in range(N+1)]

    edges = list(map(int,input().split()))
    # 그래프에 간선정보 update
    for i in range(0,len(edges),2):
        graph[edges[i]][edges[i+1]] = 1
        graph[edges[i+1]][edges[i]] = 1
        graphL[edges[i]].append(edges[i+1])
        graphL[edges[i+1]].append(edges[i])

    visited = [0]*(N+1)


    result = 0

    # 방문 안한 곳이 있다면, 한 개의 조임
    for i in range(1,N+1):
        if visited[i] == 0:
            stack = [i]
            visited[i] = 1
            result += 1
            while stack:
                cur = stack[-1]

                for neighbor in graphL[cur]:
                    if visited[neighbor]==0 :
                        stack.append(neighbor)
                        visited[neighbor] = 1
                        break
                else:
                    stack.pop()
    print(f"#{tc} {result}")
