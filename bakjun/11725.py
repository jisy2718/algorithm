N = int(input())
E = [list(map(int, input().split())) for _ in range(N - 1)]
visited = [False] * (N - 1)

arr = [0] * (N + 1)  # index가 자식 node, value가  부모 node
from collections import deque

queue = deque()
parent = 1  # 부모노드
queue.append(parent)
while queue:
    parent = queue.popleft()
    # 부모가 추가된 노드를 현재노드로하고, 현재노드의 자식을 찾는다.
    remove_node = []
    for i in range(len(E)):
        e = E[i]
        if parent == e[0]  :
            # e[1]이 자식노드
            arr[e[1]] = parent  # index가 자식 node, value가  부모 node
            queue.append(e[1])

            remove_node.append(e)

        elif parent == e[1] :
            # e[0]이 자식노드
            arr[e[0]] = parent
            queue.append(e[0])

            remove_node.append(e)
    for e in remove_node:
        E.remove(e)


for i in range(2, N + 1):
    print(arr[i])