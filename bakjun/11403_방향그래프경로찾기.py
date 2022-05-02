import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
arrL = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            arrL[i].append(j)



result = [[0]*N for _ in range(N)]


for i in range(N):
    visited = [0] * N
    visited[i] = 1
    stack = [i]
    while stack:
        cur = stack[-1]
        for neighbor in arrL[cur]:
            # cycle 생긴 경우/ cycle 내부의 것들은 모두 자기 자신과 연결됨
            if neighbor in stack:
                s = stack.index(neighbor)
                for j in range(s,len(stack)):
                    result[stack[j]][stack[j]] = 1


            if visited[neighbor] == 0:
                visited[neighbor] = 1
                stack.append(neighbor)
                break
        # 더 이상 경로 없음
        else:
            # print(stack)
            for j in range(len(stack)-1):
                for k in range(j+1,len(stack)):
                    result[stack[j]][stack[k]] = 1  # 해당 경로 존재
            stack.pop()

for row in result:
    print(*row)



