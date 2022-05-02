# 1. Make set
N = 6
p = [x for x in range(N + 1)]  # 스스로가 root(대표자) 가 되도록 초기화


# 2. find set
# 특정 노드 x의 대표자(root) 노드 반환
def find_set(x):
    # 구현 1
    while p[x] != x:  # 자기 자신이 부모가 아닌 경우, 부모로 이동
        x = p[x]  # 부모로 이동

    return x


def find_set2(x):
    if p[x] == x:
        return x
    else:
        return find_set2(p[x])


# 3. union(x,y)
# 두 노드를 하나의 집합으로 만들어주는 함수
# y의 대표자(root)가 x의 대표자(root)를 가리키게 함
# 즉 x의 대표자가 그대로 root / y를 포함하는 tree는 x의 subtree
def union(x, y):
    root_of_x = find_set(x)
    root_of_y = find_set(y)
    p[root_of_y] = root_of_x  # y의 대표자(root)가, x의 대표자(root)를 가리키도록


# 4. 위의 표 결과 실행
union(1, 3)
print(p[1:])
union(2, 3)
print(p[1:])
union(5, 6)
print(p[1:])
print(find_set(6))