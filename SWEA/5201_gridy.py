

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())

    # 화물 무게
    W = list(map(int,input().split()))

    # 트럭 적재용량
    T = list(map(int,input().split()))

    # 화물 무게, 트럭 적재용량 가장 큰 것부터 이용할 것
    W.sort()
    T.sort()

    # 트럭 적재용량에 실릴 수 있는, 가장 무거운 화물을 운반
    # 그 후, 다음 트럭 적재용량보다 큰 것은 못옮기고, 그 다음 작은 것 찾기

    result = 0
    # 화물이나 트럭 둘 중 하나가 없으면, 더이상 운반 못함
    while W and T:
        max_truck = T.pop()
        max_idx = 0
        for i in range(len(W)-1,-1,-1):
            max_weight = W[i]
            if max_weight <= max_truck: # 운반 가능
                max_idx = i # i 번 인덱스 위로는 모두 버려야 함
                result += max_weight
                break

        W = W[:i]


    print(f"#{tc} {result}")





