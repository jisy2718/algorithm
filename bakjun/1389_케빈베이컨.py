#
# import sys
# input = sys.stdin.readline
# N, M = map(int,input().split())
# INF = 0xfffffffffff
# arr = [[INF]*(N+1) for _ in range(N+1)]
#
# for _ in range(M):
#     s, e = map(int,input().split())
#     arr[s][e] = 1
#     arr[e][s] =1
#
#
# def dijk(start):
#     cur_min = arr[start].copy()
#     cur_min[start] = 0
#     visited = [0]*(N+1)
#     visited[start] = 1
#     cnt = 0
#     result = 0
#     baken = 0
#     q = []
#     while cnt != N-1:
#         for i in range(1,N+1): # 방문한 애들 중에서
#             for j in range(1, N+1):
#                 if visited[i] == 1:
#                     if arr[i][j] == 1 and visited[j]==0:
#                         q.append(j)
#                         cnt += 1
#
#         baken += 1
#         while q:
#             visit = q.pop()
#             visited[visit] = 1
#             result += baken
#         # print(result)
#
#
#     return result
#
# min_result = 0xfffffffff
# min_person = -1
#
# for i in range(1,N+1):
#     cur_result = dijk(i)
#     # print(i, cur_result)
#     if cur_result < min_result:
#         min_result = cur_result
#         min_person = i
#     elif cur_result == min_result and i < min_person:
#         min_person = i
#
# print(min_person)
#
#
#
#
#


import sys
input = sys.stdin.readline
N, M = map(int,input().split())
INF = 0xfffffffffff
arr = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    s, e = map(int,input().split())
    arr[s][e] = 1
    arr[e][s] =1

from collections import deque
def bfs(start):
    q = deque()
    q.append([start,0])
    visited = [0]*(N+1)
    visited[start] = 1
    result = 0
    while q:
        cur_node, dist = q.popleft()
        result += dist

        for i in range(1,N+1):
            if arr[cur_node][i] == 1 and visited[i] == 0:
                q.append([i,dist+1])
                visited[i] = 1

    return result

min_result = 0xffffffff
min_person = -1
for i in range(1,N+1):
    cur_result = bfs(i)

    if min_result > cur_result:
        min_result = cur_result
        min_person = i

    elif min_result == cur_result and min_person >i:
        min_person = i
print(min_person)

