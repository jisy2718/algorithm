def post_order(v):
    result = 0
    if v <= N:
        result = tree[v] # 이미 자신이 가지고 있는 값

        left_val = post_order(v*2) # 왼쪽자식
        right_val = post_order(v*2+1)    # 오른쪽 자식

        # action : 왼쪽자식과 오른쪽 자식의 값을 더해서, 자신에게 입력
        result += left_val + right_val
        tree[v] = result
        #print(result)
    return result  # node v의 value 반환


T = int(input())
for tc in range(1,T+1):
    N, M, L = map(int,input().split()) # 노드개수, 리프 노드 개수, 값을 출력할 노드 번호


    # 트리 생성 및 채우기
    # index가 node번호/ value가 node의 value
    tree = [0]*(N+1)

    for _ in range(M):
        node_num, node_value = map(int,input().split())
        tree[node_num] = node_value


    # post order로 오면서 값 넣어주기
    post_order(1)
    print(f'#{tc} {tree[L]}')

