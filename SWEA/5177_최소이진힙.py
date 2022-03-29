def push(value):
    # 1. 이진트리 생성 (idx를 차례로 증가시키며 가져와서)
    global last

    tree[last+1] = value
    last+=1
    child = last
    parent = child//2
    # 2. 부모와 값 비교해서, 최소로 맞추기
    # 만약 부모 노드의 value보다 작다면 부모와 교환
    # 이를 반복
    while parent >= 1 and tree[child] < tree[parent]: # 삽입노드(idx번째)가 root되면 그만
        # 자식, 부모 = 부모, 자식
        tree[child], tree[parent] = tree[parent], tree[child] # 값 교환
        child = parent
        parent = child//2 # 삽입된 노드의 새로운 idx





T = int(input())
for tc in range(1,T+1):
    # 1. input 받기
    N = int(input())
    values = [0] + list(map(int,input().split()))
    # print(f'values len {len(values)} {values}')
    # 2. value 하나마다 push 해주기
    tree = [0]*(N+1)
    last = 0
    for idx in range(1,len(values)):
        # print(idx)
        value = values[idx]
        push(value)

    # print(tree)


    # 조상찾기
    result = 0
    #print(last,tree)
    cur = last//2
    while cur >= 1: # 루트로 갈때까지
        result += tree[cur]
        cur //= 2

    print(f'#{tc} {result}')

