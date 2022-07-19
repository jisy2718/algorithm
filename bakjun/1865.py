
def bellman_ford(start):
    dist[start] = 0

    for i in range(N):
        # 모든 간선에 대해서, 새로운 이동거리가 더 짧을 수 있는지 확인
        for j in range(len(arr)):
            cur = arr[j][0]
            next_node = arr[j][1]
            d = arr[j][2]
            # 만약 cur -> next_node 비용이 기존의 dist[next_node] 보다 적으면 갱신
            if dist[cur] + d < dist[next_node] and dist[cur] != INF:  # 이동가능해야하므로 !INF
                dist[next_node] = dist[cur] + d
                if i == N - 1:
                    return True  # 음의 순환 존재
    return False

T = int(input())
INF = 0XFFFFFFFFFF
for _ in range(T):
    # input 방법
    # arr = [[start, end, distance], ..., ...]


    N, M, W = map(int,input().split())  # 지점수 N, 도로수 M, 웜홀수 W
    arr = []
    arr2 = [[INF]*(N+1) for _ in range(N+1)]

    # 도로정보
    for _ in range(M):
        S, E, T = map(int,input().split()) # 시작, 끝, 시간  /양방향
        arr.append([S,E,T])
        arr.append([E,S,T])
        arr2[S][E] = T
        arr2[E][S] = T


    # 웜홀정보
    for _ in range(W):
        S, E, T = map(int,input().split()) # 시작, 끝, 줄어드는 시간 / 편도
        arr.append([S,E,-T])
        arr2[S][E] = -T




    # 모든 경우에 자기 자신으로 돌아오는 것이 음수로 가능한지 확인
    flag = False  # 이동 가능한 지 확인하는 것
    for v in range(1, N+1):
        dist = [INF] * (N + 1)
        bellman_ford(v)
        # print(dist)
        for next_v in range(1,N+1):
            if next_v != v:
                if dist[next_v] + arr2[next_v][v] <0:  # v -> next_node -> v 순서로 움직임
                    print("YES")
                    flag = True
                    break
        if flag == True:
            break

    else:
        print("NO")

