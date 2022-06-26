

from collections import deque

A, B = map(int,input().split())
q = deque()
# 수가 커지는 연산만 가능하므로, 여기까지 하면됨. 작아지는 연산도 있으면, 그에 알맞게 더 크게 잡아줘야
visited = [-2]*(B+1)

q.append([A,0])

visited[A] = 0

while q:
    cnum, cmove = q.popleft()
    if cnum == B:

        break

    nnum1 = cnum*2
    nnum2 = cnum*10 + 1

    if nnum1 <= B and (visited[nnum1]==-2 or visited[nnum1]>cmove+1)  : # 방문하지 않았거나, 더 짧게 방문가능하면 방문
        q.append([nnum1, cmove+1])
        visited[nnum1] = cmove+1


    if nnum2 <=  B and (visited[nnum2]==-2 or visited[nnum2]>cmove+1) :
        q.append([nnum2, cmove+1])
        visited[nnum2] = cmove+1


print(visited[B]+1)