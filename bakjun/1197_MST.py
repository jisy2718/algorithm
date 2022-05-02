

V, E = map(int,input().split())
edges = []
for _ in range(E):
    s, e, w = map(int,input().split())
    edges.append([w, s, e])

# make set
p = [x for x in range(V+1)]

# find set
def find_set(x):
    if p[x] == x:
        return x
    else:
        return find_set(p[x])



def union(x,y):
    root_x = find_set(x)
    root_y = find_set(y)
    p[root_y] = root_x

MST = list(range(1,V+1))
w_sum = 0
# sorting
# cycle 안생기면 선택
# 다 선택하면 끝

edges.sort()
for i in range(E):
    w, s, e = edges[i]
    if find_set(s) != find_set(e):
        union(s,e)
        w_sum += w
print(w_sum)


#--------------------------------------인접리스트 버전--------------------------------------
# V, E = map(int,input().split())
# arrL = [[]*(V+1) for _ in range(V+1)]
# for _ in range(E):
#     s, e, w = map(int,input().split())
#     arrL[s].append([e,w])
#     arrL[e].append([s,w])
#
# def prim(start):
#     MST = [0] * (V + 1)
#
#     # 1 번노드에서 시작한다고 가정
#
#     # 1번노드에서 이동할 수 있는 최소거리 노드 x 로 이동
#
#     # 1, x번 노드에서 이동할 수 있는 최소거리노드 x2로 이동
#     # MST에 포함되지 않아야 함
#
#     #... 이를 반복
#
#     MST[start] = 1
#     w_sum = 0
#     for _ in range(1,V): # start 제외 V-1 개 경로 고르면 됨
#         min_idx = 0
#         min_val = 0xfffffffff
#         for i in range(1,V+1):
#             if MST[i] == 1:
#                 for end_weight in arrL[i]:
#                     e, w = end_weight
#                     if min_val > w and MST[e]==0:
#                         min_val = w
#                         min_idx = e
#         MST[min_idx] = 1
#         w_sum += min_val
#
#     print(w_sum)
#
# prim(1)

#----------------------------------------------------------------------------------------------------------





#------------------------------------------------arr 버전------------------------------------
# V, E = map(int,input().split())
# arr = [[0]*(V+1) for _ in range(V+1)]
#
# for _ in range(E):
#     s, e, w = map(int,input().split())
#     arr[s][e] = w
#     arr[e][s] = w
#
# def prim(start):
#     MST = [0] * (V + 1)
#     # 1 번노드에서 시작한다고 가정
#     # 1번노드에서 이동할 수 있는 최소거리 노드 x 로 이동
#     # 1, x번 노드에서 이동할 수 있는 최소거리노드 x2로 이동
#     # MST에 포함되지 않아야 함
#     #... 이를 반복
#     MST[start] = 1
#     w_sum = 0
#     for _ in range(1,V):
#         min_idx = 0
#         min_val = 0xfffffffff
#         for i in range(1,V+1):
#             if MST[i] == 1:
#                 for j in range(1,V+1):
#                     if min_val > arr[i][j] and MST[j]==0:
#                         min_val = arr[i][j]
#                         min_idx = j
#         MST[min_idx] = 1
#         w_sum += min_val
#
#     print(w_sum)
#
# prim(1)
# --------------------------------------------------------------------------------------
