import sys
sys.stdin = open('1231_input.txt')

for tc in range(1, 11):
    V = int(input())

    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    alpha = [0] * (V + 1)

    # 자료 저장
    for _ in range(V):
        v_info = list(input().split())
        cur_node = int(v_info[0])
        cur_node_alpha = v_info[1]
        alpha[cur_node] = cur_node_alpha  # 해당 node 의 alphabet 저장
        if len(v_info) >= 3:
            ch1[cur_node] = int(v_info[2])
            if len(v_info) == 4:
                ch2[cur_node] = int(v_info[3])

    # print(ch1, ch2, alpha)
    def in_order(v):
        if v:  # 0 초과경우
            in_order(ch1[v])
            print(alpha[v], end='')
            in_order(ch2[v])

    print(f'#{tc}', end= ' ')

    in_order(1)
    print()