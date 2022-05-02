# 자식이 존재하는지 안하는지 가서 확인해보는 코드
# complet_binary_tree_traversal.py 는 자식이 존재하는 경우에만 이동

# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
# 1 2 / 1 3 / 2 4 / 3 5 / 3 6 / 4 7 / 5 8 / 5 9 / 6 10 / 6 11 / 7 12 / 11 13

N = int(input())

arr = [[0]* (N+1) for _ in range(2)]

E = list(map(int,input().split()))

for i in range(0, len(E),2):
    parent, child = E[i], E[i+1]
    # print(parent, child)
    if arr[0][parent]:
        arr[1][parent] = child
    else:
        arr[0][parent] = child
# print(arr)

# visited
visited = [False]*(N+1)


# 전위 순회

# 자신 / 좌 / 우 순으로 순회
def preorder(T):
    if T: # 0이 아닌경우
        visited[T] = True
        print(T, end=' ')
        preorder(arr[0][T]) # 왼 자식
        preorder(arr[1][T]) # 오른 자식
    return

def inorder(T):
    if T: # 0이 아닌경우
        inorder(arr[0][T])
        visited[T] = True
        print(T, end= ' ')
        inorder(arr[1][T])
    return


def postorder(T):
    if T: # 0이 아닌경우
        postorder(arr[0][T])
        postorder(arr[1][T])
        visited[T] = True
        print(T, end= ' ')
    return
preorder(1)
print()
inorder(1)
print()
postorder(1)



