N, M = map(int,input().split())
t_nodes = list(map(int,input().split()))

# 해당 노드들이 없는 그룹의 개수를 찾아야 함
except_nodes = t_nodes[1:]

arr = [[0]*(N+1) for _ in range(N+1)]

parties = []
# graph 만들기
for _ in range(M):
    nodes = list(map(int,input().split()))
    num = nodes[0]
    parties.append(nodes[1:])
    for i in range(1,num+1):
        for j in range(i,num+1):
            arr[nodes[i]][nodes[j]] = 1
            arr[nodes[j]][nodes[i]] = 1

# print(parties)


make_set = list(range(N+1))
# print(make_set)
def find_root(a):
    if make_set[a] == a:
        return a

    else:
        return find_root(make_set[a])

def union(a,b):
    a_root = find_root(a)
    b_root = find_root(b)
    # print(f'a,b roots {a_root}, {b_root}')
    # print('*',make_set)
    make_set[b_root] = a_root
    # print(make_set)


# graph 병합
for i in range(1,N+1):
    for j in range(i+1,N+1):
        # print('i,j are : ', i,j, 'arr[i][j] is ', arr[i][j])

        if arr[i][j] == 1:
            union(i,j)

# print(make_set)

# 진실을 아는 사람들의 root 노드 찾아주기
root_set = set()
for node in except_nodes:
    root = find_root(node)
    root_set.add(root)

# 거짓말 할 수 있는 파티의 수
# 거짓말 할 수 있는 파티 = 각 파티의 모든 사람의 root가 root_set에 포함되지 않으면 됨
result = 0
for party in parties:
    # 전체 구성원들의 root가 root_set에 없어야지만 거짓말 가능
    for node in party:
        if find_root(node) in root_set:
            break
    else:
        result += 1

print(result)
