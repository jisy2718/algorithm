import sys
sys.stdin = open('4871_input.txt')

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    E_list = [list(map(int, input().split())) for _ in range(E)]

    target = list(map(int, input().split()))

    adj = [[0] * (V + 1) for _ in range(V + 1)]  # adj 의 idx 와 node 의 번호 맞추기 위해

    # 인접행렬 만들기
    for e in E_list:
        adj[e[0]][e[1]] = 1

    # visited 만들기
    visited = [False] * (V + 1)

    # 결과
    result = 0

    # 순회시작
    stack = []
    stack.append(target[0])
    visited[target[0]] = True
    while stack:
        cur = stack[-1]
        # 성공한 경우
        if cur == target[1]:
            result = 1
            break
        for c in range(V + 1):  # cur 행의 c 열들 중 이동 가능한 곳이 있나 파악
            if adj[cur][c] == 1 and not visited[c]:  # 연결되어있고, 이전에 방문하지 않았다면
                stack.append(c)
                visited[c] = True
                break
        else:
            # 현재 노드에서는 이동위치를 찾을 수 없음
            stack.pop()
    # 만약 while 문 다 돌았을 때, break 가 아니라 stack이 다 없어졌다면 경로를 찾지 못한 것
    print(f"#{tc} {result}")