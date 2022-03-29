import sys
sys.setrecursionlimit(10**9)
N = int(input())

in_order = list(map(int,input().split()))
post_order = list(map(int,input().split()))

in_value_index = [0]*(N+1)
for i in range(N):
    in_value_index[in_order[i]] = i

def inpost_to_pre(IS, IE, PS, PE):
    # POST ORDER의 맨뒤가 ROOT이므로, 이를 IN ORDER에서 찾기
    # 그럼 IN ORDER에서 ROOT의 좌 우가 왼편, 오른편 트리임
    # 왼쪽 트리의 노드개수, 오른쪽 트리의 노드 개수를 구해서
    # IN ORDER / POST ORDER에서 왼쪽, 오른쪽 트리 범위 구하기

    if IS > IE:# 왼쪽트리가 없거나 오른쪽 트리가 없는 경우 / 아래코드보면 왜 이 조건인지 알게됨
        return
    root = post_order[PE]
    Iroot_index = in_value_index[root]

    # pre order는 root부터 방문 후, 좌,우 방문이므로 root 먼저 찾으면 출력
    print(root, end= ' ')


    # 왼쪽 트리의 노드 개수
    left = Iroot_index - IS
    # 오른쪽 트리의 노드 개수
    right = IE - Iroot_index

    # 만약 left == 0 이라면 IS > IS + left -1
    # 만약 right == 0 이라면 IE - right +1 > IE
    # 각각 1개인 경우, 1개의 INDEX가 선택됨도 알 수 있음
    inpost_to_pre(IS, IS + left -1, PS, PS + left - 1)
    inpost_to_pre(IE-right+1, IE, PE - right , PE -1 )


inpost_to_pre(0,N-1,0,N-1)

