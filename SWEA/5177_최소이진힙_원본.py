def push(value, idx):
    # 1. 이진트리 생성 (idx를 차례로 증가시키며 가져와서)

    tree[idx] = value
    c = value # 현재 노드
    # 2. 부모와 값 비교해서, 최소로 맞추기
    p = tree[idx//2]  # 부모의 값
    # 현재 삽입된 idx 번째 노드의 value가 부모노드의 value보다 크다면 ok
    # 만약 부모 노드의 value보다 작다면 부모와 교환
    # 이를 반복
    while idx > 1 and tree[idx] < tree[idx//2]: # 삽입노드(idx번째)가 root되면 그만
        # 자식, 부모 = 부모, 자식
        tree[idx], tree[idx//2] = tree[idx//2], tree[idx] # 값 교환
        idx = idx//2 # 삽입된 노드의 새로운 idx





T = int(input())
for tc in range(1,T+1):
    # 1. input 받기
    N = int(input())
    values = [0] + list(map(int,input().split()))
    # print(f'values len {len(values)} {values}')
    # 2. value 하나마다 push 해주기
    tree = [0]*(N+1)
    for idx in range(1,len(values)):
        # print(idx)
        value = values[idx]
        push(value, idx)

    # print(tree)


    # 조상찾기
    result = 0
    cur = len(values)//2
    while cur >= 1: # 루트로 갈때까지
        result += tree[cur]
        cur //= 2

    print(f'#{tc} {result}')

