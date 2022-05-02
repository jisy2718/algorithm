tc = 0
while True:
    tc += 1
    n, m = map(int,input().split())


    if n == 0 and m == 0:
        break


    graph = [[0]*(n+1)] +[ [0]*(n+1) for _ in range(n+1)]
    visited = [False]*(n+1)
    edge_visited = [[False]*(n+1) for _ in range(n+1)]

    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1][v2] = 1
        graph[v2][v1] = 1


    # 2. 전체노드 FOR LOOP 내부에서 DFS 진행
    # DFS 중 VISTED 된 노드가 중복되어서 생기면 그 부분은 트리가 아님

    result = 0
    for v in range(1,n+1):
        if visited[v] == False:
            tree = True

            stack = [v]
            visited[v] = True
            while stack:
                cur_v = stack.pop()

                for neighbor_v in range(1,n+1):
                    if graph[cur_v][neighbor_v] == 1 and edge_visited[cur_v][neighbor_v] == False: # 이웃이고, 왔던 경로가 아닌 경우
                        if visited[neighbor_v] == True: # cycle 존재
                            tree = False
                        # 정상적인 경우
                        else:
                            stack.append(neighbor_v)
                            visited[neighbor_v] = True
                            edge_visited[cur_v][neighbor_v] = 1
                            edge_visited[neighbor_v][cur_v] = 1
            if tree == True:
                result += 1


if result == 0:
    print(f'Case {tc}: No trees.')
elif result == 1:
    print(f'Case {tc}: There is one tree.')
else:
    print(f'Case {tc}: A forest of {result} trees.')

#-------------------------------------------------------------------------------------
import sys
input = sys.stdin.readline
tc = 0
while True:
    tc += 1
    n, m = map(int,input().split())

    if n == 0 and m == 0:
        break
    graph = [ []*(n+1) for _ in range(n+1)]
    visited = [False]*(n+1)

    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)



    make_set = [x for x in range(n+1)]

    def find_set(x):
        if make_set[x] == x:
            return x
        else:
            return find_set(make_set[x])

    def union(x,y):
        root_x = find_set(x)
        root_y = find_set(y)
        make_set[root_y] = root_x


    # 사이클 생기면 1개 제외 !
    non_tree = []

    for v in range(1, n+1):
        for neighbor in graph[v]:
            if find_set(v) == find_set(neighbor):
                non_tree.append(find_set(v))
            union(v, neighbor)
    # print(make_set)


    # 전체 덩어리 개수
    count = 0
    for x in range(1,n+1):
        if x == make_set[x]:
            count += 1

    # tree 가 아닌 것 개수 (사이클 있는 것 개수)
    non_tree_root = set()
    for x in non_tree:
        non_tree_root.add(find_set(x))

    result = count - len(non_tree_root)

    if result == 0:
        print(f'Case {tc}: No trees.')
    elif result == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {result} trees.')
