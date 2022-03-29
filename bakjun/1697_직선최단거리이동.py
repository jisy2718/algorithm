from collections import deque

N, K = map(int, input().split())
# N에서 +=1 하거나 2N 하여 K로 가장빨리 가야함
visited = [False]*(2*max(N,K))
queue = deque()
queue.append([N, 0])

while queue:
    c_loc, c_time = queue.popleft()

    if c_loc == K:
        print(c_time)
        break

    elif c_loc > K:
        if visited[c_loc -1] == False:
            queue.append([c_loc - 1, c_time + 1])
            visited[c_loc-1]  = True
    else:
        # 방문 가능 경우의 수
        move = [c_loc-1, c_loc+1, c_loc*2]
        for m in move:
            if 0<= m <= 2*max(K,N) and visited[m] == False:
                queue.append([m, c_time + 1])
                visited[m] = True
