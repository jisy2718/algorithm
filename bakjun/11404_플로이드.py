import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    i,j,w = map(int,input().split())
    arr[i].append((j,w))



# 모든 경우에 다익스트라 구현

def dijk(start):
    # 1. 초기화 : 비용 list 생성 , 방문 set 생성, 앞 2가지 초기화
    INF = 0xfffffffffff
    cost = [INF]*(N+1)
    visited = set()

    cost[start] = 0
    visited.add(start)

    for neighbor in arr[start]:
        node, weight = neighbor
        if cost[node] > weight:  # 여러 연결 선이 있을 수 있으므로
            cost[node] = weight

    while len(visited) <N: # 모든 곳을 방문하지 못한 경우에 진행 / while 문 들어가자마자, 방문할 곳 없는 경우도 고려하기
        # print(f'start is {start}, cost is {cost}')
        # 2. 다익스트라 진행
        # 최소 비용인 곳으로 이동
        min_idx = -1
        min_cost = INF
        for idx in range(1,N+1):
            # 방문하지 않은 곳 중 최소비용
            if idx not in visited and cost[idx] < min_cost:
                min_idx = idx
                min_cost = cost[idx]


        # 최소 비용인 곳으로 이동 후, 이동 비용 업데이트
        if min_idx == -1:
            break
        else:
            visited.add(min_idx)

        # 새로 이동한 곳에서 연결된 곳들을 기존의 것과 비교하기
        # 새로이동한 곳까지의 비용 + 새로 이동한 곳에서 다른 곳(a)까지 비용 < 기존의 a 까지의 비용 인 경우 업데이트
        for neighbor in arr[min_idx]:
            node_a, weight = neighbor
            # 기존에 방문 했던 곳은 알고리즘 구조 상 업데이트 되지 않으므로, visited는 고려안해줘도 됨
            if min_cost + weight < cost[node_a]:
                cost[node_a] = min_cost + weight



        # 3. 다익스트라 과정 중, while문 break 조건 넣어주기
        # 만약 cost list의 INF가 아닌 것들이 모두, visited set에 포함되어 있다면, 더 이상 이동할 곳 없으므로 break
        flag = True
        for node in range(1,N+1):
            if cost[node] != INF and node not in visited:
                break
        else:
            flag = False

        if flag == False:
            break
    # while 문 끝-----------------------

    # 4. INF => 0으로 바꾸고, 자기 자신 빼고 비용 print
    for i in range(1,N+1):
        if cost[i] == INF:
            cost[i] = 0
        print(cost[i], end=' ')
    print()



for i in range(1,N+1):
    dijk(i)


