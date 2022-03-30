import sys
from collections import deque
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    graph = [[0] * (n + 1)] + [[0] * (n + 1) for _ in range(n + 1)]
    visited = [False] * (n + 1)
    # edge_visited = [[False] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1][v2] = 1
        graph[v2][v1] = 1
    # for row in graph:
    #     print(row)

    # 2. 전체노드 FOR LOOP 내부에서 DFS 진행
    # DFS 중 VISTED 된 노드가 중복되어서 생기면 그 부분은 트리가 아님

    result = 0
    for v in range(1, n + 1):
        if visited[v] == False:
            tree = True

            queue = deque()
            queue.append(v)

            while queue:
                cur = queue.popleft()
                if visited[cur] == True:
                    tree = False
                    # print(visited, cur)
                visited[cur] = True

                for neighbor in graph[cur]:
                    if graph[cur][neighbor] == 1 and visited[neighbor]== False:
                        queue.append(neighbor)


            if tree==True:
                result += 1
    if result == 0:
        print("Case 3: No trees.")
    elif result == 1:
        print("Case 2: There is one tree.")
    else:
        print(f"Case 1: A forest of {result} trees.")