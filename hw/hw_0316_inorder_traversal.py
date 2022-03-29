
# 완전 이진 트리의 in_order
def in_order(v):
    if v <= N: # 최대 노드 개수 N으로 주어짐
        in_order(v*2) #좌측자식
        print(tree[v],end='')
        in_order(v*2 + 1) # 우측자식



for tc in range(1, 2):

    N = int(input())
    tree = [0] * (N + 1)

    # 자료 저장
    for _ in range(N):
        v_info = list(input().split())
        cur_node = int(v_info[0])
        cur_node_alpha = v_info[1]
        tree[cur_node] = cur_node_alpha


    print(f'# {tc}', end=' ')
    in_order(1)
    print()