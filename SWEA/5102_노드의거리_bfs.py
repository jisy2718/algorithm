import sys
sys.stdin = open('5102_input.txt')

# start 에서 시작해서 end로 끝나는 최단거리
def bfs(start, end, V, adj):
    queue = []
    queue.append([start,0])
    visited = [False] * (V + 1)
    while queue:
        front, distance = queue.pop(0)
        if front == end:
            return distance

        for node in range(1, V + 1):
            if adj[front][node] == 1 and visited[node] == False:
                visited[node] = True
                queue.append([node,distance+1])

    return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    adj = [[0] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        r, c = map(int, input().split())
        adj[r][c] = 1
        adj[c][r] = 1

    start, end = map(int, input().split())
    result = bfs(start, end, V, adj)
    print(f"#{tc} {result}")