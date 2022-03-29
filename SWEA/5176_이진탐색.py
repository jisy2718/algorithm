def in_order(v):
    global value
    if v<=N:
        in_order(v*2)
        tree[v] = value
        value += 1
        in_order(v*2+1)


T = int(input())
for tc in range(1,T+1):
    N = int(input())

    value = 1 # inorder 순으로 value 넣어줄것
    tree = [0]*(N+1) # index를 노드번호로함
    in_order(1)
    # 결과 출력 ( 루트, N//2 번노드)

    print(f'#{tc} {tree[1]} {tree[N//2]}')

