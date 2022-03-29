import sys
sys.stdin = open('1952_input.txt')

T = int(input())
for tc in range(1, T+1):
    d, m, m3, y = map(int,input().split())
    plan = [0] + list(map(int,input().split())) # 1~ 12월을 index로 이용

    cur_min = y # 1년이용권을 우선 최저 가격이라고 초기값
    cost = 0
    not_paid_month = 1
    queue = [[not_paid_month, cost]]
    # print(queue)
    while queue:
        cnpm, cc = queue.pop(0)
        # 각 달을 결제하면, plan의 각 달을 0으로 만들자.
        if cnpm <= 12:
            if plan[cnpm] == 0:
                queue.append([cnpm+1,cc])

            else:
                # 1) 1일 결제
                nc = cc + plan[cnpm]*d # 현재까지비용
                queue.append([cnpm+1, nc])

                # 2) 1달 결제
                nc = cc + m
                queue.append([cnpm+1, nc])
                # 3) 3달 결제
                nc = cc + m3
                queue.append([cnpm+3, nc])

        else:
            if cur_min > cc:
                cur_min = cc

    print(f'#{tc} {cur_min}')

