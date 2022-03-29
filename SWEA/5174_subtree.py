def pre_order(v):
    global result
    if v:
        result += 1
        pre_order(tree[0][v])
        pre_order(tree[1][v])

T = int(input())
for tc in range(1,T+1):
    E, N = map(int,input().split())

    edges = list(map(int,input().split()))  # 부모 자식 부모 자식 꼴


    # tree 생성
    tree = [ [0]*(E+2) for _ in range(2)]  # index 가 부모

    for i in range(0,len(edges)//2):

        if tree[0][edges[2*i]] == 0 :
            tree[0][edges[2*i]] = edges[2*i+1]
        else:
            tree[1][edges[2*i]] = edges[2*i + 1]
        # print(tree)



    # N 부터 탐색하며 더하기
    result = 0
    pre_order(N)

    print(f'#{tc} {result}')

