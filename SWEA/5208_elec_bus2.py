# def dfs(cur, charge_cnt):
#     global result
#     # 도착한 경우
#     if cur == N:
#         if result > charge_cnt - 1: # 도착지에서는 충전 안함
#             result = charge_cnt - 1
#         return
#     elif cur > N:
#         return
#
#     fuel = stations[cur]
#
#
#     for i in range(1,fuel+1):# 운행가능 구간
#         dfs(cur+i,  charge_cnt+1)
#
#
#
# T = int(input())
# for tc in range(1,T+1):
#     stations = list(map(int,input().split()))
#     N = stations[0]
#     start = 1
#     result = N
#
#     dfs(1,0)
#     print(f"#{tc} {result}")


def dfs(cur, charge_cnt):
    global result
    # 도착한 경우
    fuel = stations[cur]
    if cur + fuel >= N:
        if result > charge_cnt :  # 도착지에서는 충전 안함
            result = charge_cnt
        return



    # 갈 수 있는 거리 중, 충전소에서 교체시, 가장 멀리 갈 수 있는 곳으로 이동
    move = 1
    max_loc = cur + 1 # 그냥 초기값
    for i in range(1, fuel + 1):  # 운행가능 구간
        loc = stations[cur+i] + cur+i
        if loc > max_loc:
            max_loc = loc
            move = i


    dfs(cur + move, charge_cnt + 1)


T = int(input())
for tc in range(1, T + 1):
    stations = list(map(int, input().split()))
    N = stations[0]
    start = 1
    result = N

    dfs(1, 0)
    print(f"#{tc} {result}")