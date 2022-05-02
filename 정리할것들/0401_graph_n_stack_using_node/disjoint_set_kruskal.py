# 상호 베타 집합을 구현하기 위한 연산
# union : 두 개의 집합을 하나로 만들어주는 연산 ( 두 개의 집합의 대표자를 1개로 만듦 / root만 가리키는 곳 바꿔주면 됨)
# find_set : 집합의 대표자를 반환하는 연산

# 자식노드를 index, 부모노드를 value로 하는 트리 생성

N = 7
p = [x for x in range(N+1)] # 스스로가 root(대표자) 가 되도록 초기화
# 특정 노드 x의 대표자(root) 노드 반환
def find_set(x):
    # 구현 1
    while p[x] != x: # 자기 자신이 부모가 아닌 경우, 부모로 이동
        x = p[x]     # 부모로 이동

    return x

def find_set2(x):
    if p[x] == x:
        return x
    else:
        return find_set2(p[x])


# 두 노드를 하나의 집합으로 만들어주는 함수
# y의 대표자가 x의 대표자를 가리키게 함 / 즉 x의 대표자가 그대로 root / y를 포함하는 tree는 x의 subtree
def union(x,y):
    root_of_x = find_set(x)
    root_of_y = find_set(y)
    p[root_of_y] = root_of_x  # y의 대표자가, x의 대표자를 가리키도록


print(p)
union(3,4)
print(p)
union(0,4)
print(p)
union(0,7)
print(p)



def bubble_sort(edge_info):
    for i in range(E):  # 비교노드 시작지점
        for j in range(i, E-1): # 비교노드와 비교하는 노드들
            if edge_info[j][2] > edge_info[j+1][2]:
                edge_info[j], edge_info[j+1] = edge_info[j+1], edge_info[j]



#---------------------kruscal algorithm----------------------------

INF = 10000000
V, E = map(int,input().split())

# kruscal(크루스칼) 은  시작 - 종료 - 비용 정보가 필요
edge_info = []

for _ in range(E):
    s, e, w = map(int,input().split()) # 간선의 시작, 종료, 비용
    edge_info.append((s,e,w))

print(edge_info)
p = [x for x in range(V)]
def kruscal(edge_info):
    mst = []
    edge_info.sort(key=lambda x: x[2])

    mst = []
    for i in range(E):
        # 두 개의 노드가 사이클이 생기지 않으면, MST에 추가
        if find_set(edge_info[i][0]) == find_set(edge_info[i][1]): # 이미 대표자가 같다면, 연결시 사이클 생김
            continue
        # 연결 안된 것 발견시, 이것이 최소비용이므로, 바로 추가
        mst.append(edge_info[i])
        union(edge_info[i][0], edge_info[i][1])  # 추가된 간선들 root(대표자) 변경

    return mst


# 7 11
# 0 1 32
# 0 2 31
# 0 5 60
# 0 6 51
# 1 2 21
# 2 4 46
# 2 6 25
# 3 4 34
# 3 5 18
# 4 5 40
# 4 6 51
print(kruscal(edge_info))



# heap 이용해서 구현
import heapq
for _ in range(E):
    s, e, w = map(int,input().split()) # 간선의 시작, 종료, 비용
    heapq.heappush(edge_info,(w,s,e))

def kruscal_heap(edge_info):
    mst = []

    w, s, e = heapq.heappop(edge_info) # 최소힙 팝
    if find_set(s) == find_set(e): # s와 e가 대표자가 같다는 것이므로, 이미 연결된 경우
        # continue
        pass
