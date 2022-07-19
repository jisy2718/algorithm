

N, M = map(int,input().split())
length = 100000

from collections import deque


# 1. 가장 빠른 시간을 구하고

q = deque()
q.append(N)
visited = [-1]*(length+1)
visited[N] = 0

while q:
    c = q.popleft()
    move = visited[c]
    if c == M:
        break

    else:
        if 0<= c + 1 <= length and visited[c+1] == -1:
            q.append(c+1)
            visited[c+1] = move + 1

        if 0 <= c-1 <= length and visited[c-1] == -1:
            q.append(c-1)
            visited[c-1] = move + 1

        if 0 <= 2*c <= length and visited[2*c] == -1:
            q.append(2*c)
            visited[2*c] = move+ 1


# 2. 가장 빠른시간으로 갈 수 있는 방법을 백트래킹으로 찾기
shortest = visited[M]

count = 0

q = deque()

q.append(N)
visited = [-1]*(length+1)
visited[N] = 0

while q:
    c = q.popleft()
    move = visited[c]
    if move > shortest:  #백트래킹
        continue

    if c == M:
        count += 1
        # print('count +1 = ', count)

    else:
        if 0<= c + 1 <= length and (visited[c+1] == -1 or visited[c+1] == move + 1):
            q.append(c+1)
            visited[c+1] = move + 1

        if 0 <= c-1 <= length and (visited[c-1] == -1 or visited[c-1] == move + 1):
            q.append(c-1)
            visited[c-1] = move + 1

        if 0 <= 2*c <= length and (visited[2*c] == -1 or visited[2*c] == move + 1):
            q.append(2*c)
            visited[2*c] = move+ 1



print(shortest)
print(count)







#
#
# N, M = map(int,input().split())
#
#
# from collections import deque
# # 1. 가장 빠른 시간을 구하고
#
# q = deque()
# kind = 1
# q.append((N,kind))
# visited = [-1] * 100001
# visited[q] = 0
#
#
# while q:
#     loc, cur_kind = q.popleft()
#     move = visited[loc]
#     if loc == M:
#         continue
#
#     else:
#         if 0 <= loc + 1 <= 100000 and visited[loc + 1] == -1 or visited[loc+1]==move+1:
#             q.append(loc + 1)
#             visited[loc + 1] = move + 1
#
#         if 0 <= loc - 1 <= 1000000 and visited[loc - 1] == -1:
#             q.append(loc - 1)
#             visited[loc - 1] = move + 1
#
#         if 0 <= 2 * loc < 100000 and visited[2 * loc] == -1:
#             q.append(2 * loc)
#             visited[2 * loc] = move + 1
#
#
