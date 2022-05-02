#-------------------------------------------------------------------------------
# N = int(input())
# E = [list(map(int, input().split())) for _ in range(N - 1)]
# visited = [False] * (N - 1)
#
# arr = [0] * (N + 1)  # index가 자식 node, value가  부모 node
# from collections import deque
#
# queue = deque()
# parent = 1  # 부모노드
# queue.append(parent)
# while queue:
#     parent = queue.popleft()
#     # 부모가 추가된 노드를 현재노드로하고, 현재노드의 자식을 찾는다.
#     remove_node = []
#     for i in range(len(E)):
#         e = E[i]
#         if parent == e[0]  :
#             # e[1]이 자식노드
#             arr[e[1]] = parent  # index가 자식 node, value가  부모 node
#             queue.append(e[1])
#
#             remove_node.append(e)
#
#         elif parent == e[1] :
#             # e[0]이 자식노드
#             arr[e[0]] = parent
#             queue.append(e[0])
#
#             remove_node.append(e)
#     for e in remove_node:
#         E.remove(e)
#
#
# for i in range(2, N + 1):
#     print(arr[i])
#
#----------------------------------------------------------------------------------------------
#------------시간초과-------------------
# N = int(input())
# E = [list(map(int, input().split())) for _ in range(N - 1)]
# visited = [False] * (N - 1)
# arr = [0]*(N+1)
# cur = 1
#
# def dfs(cur):
#     # 자식이 있는 경우
#     for i in range(len(E)):
#         if cur in E[i] and visited[i] == 0:
#             visited[i] = 1
#             if cur == E[i][0]:
#                 child = E[i][1]
#             else:
#                 child = E[i][0]
#             arr[child] = cur
#             break
#     # 더 이상 자식이 없는 경우
#     else:
#         return
#
#     # 자신을 먼저 마저 탐색
#     dfs(cur)
#     # 자신 탐색 끝나면 자식 탐색
#     dfs(child)
#
#     return
#
# dfs(1)
# for i in range(2,len(arr)):
#     print(arr[i])

#----------------------------------------------------------------
# def dfs(cur,E):
#     # 자식이 있는 경우
#     if not E:
#         return
#
#     for edge in E:
#         if cur in edge:
#             if cur == edge[0]:
#                 child = edge[1]
#             else:
#                 child = edge[0]
#             arr[child] = cur
#             used = edge
#             break
#     # 더 이상 자식이 없는 경우
#     else:
#         return
#     new_E = E.remove(used)
#     # 자신을 먼저 마저 탐색
#     dfs(cur, new_E)
#     # 자신 탐색 끝나면 자식 탐색
#     dfs(child, new_E)
#
#     return
#
# dfs(1,E)
# for i in range(2,len(arr)):
#     print(arr[i])


#-----------------------------------------------------------------------------
N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    e1, e2 = map(int,input().split())
    tree[e1].append(e2)
    tree[e2].append(e1)

value_is_parent = [0]*(N+1)

def dfs(cur):
    for neighbor in tree[cur]:
        if value_is_parent[neighbor] == 0:
            value_is_parent[neighbor] = cur
            dfs(neighbor)

cur = 1
dfs(cur)
for i in range(2,len(value_is_parent)):
    print(value_is_parent[i])