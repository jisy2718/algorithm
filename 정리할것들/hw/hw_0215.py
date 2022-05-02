import sys
# 표준 입력 경로 변경
sys.stdin = open("hw_0215_input.txt", 'r')

T = 10


# 좌측으로 갈 수 있다면 끝까지 가는 함수
def turn_left_and_go(cur_coordi, arr):
    r, c = cur_coordi
    while 1 <= c < 100:
        # 좌측으로 한 칸 이동
        c -= 1
        if arr[r][c] == 1:  # 이동 가능
            # 이동사항 유지
            continue

        else:  # 이동 불가시 이동사항 되돌리고 break
            c += 1
            break
    return r, c


# 우측으로 갈 수 있다면 끝까지 가는 함수
def turn_right_and_go(cur_coordi, arr):
    r, c = cur_coordi
    while 0 <= c < 99:
        # 우측으로 한 칸 이동
        c += 1
        if arr[r][c] == 1:
            # 이동사항 유지
            continue
            # 이동사항 되돌리고 break
        else:
            c -= 1
            break
    return r, c


# 위로 1칸 가는 함수
def go_upward_1cell(cur_coordi, arr):
    r, c = cur_coordi
    # 위로 진행
    r -= 1
    if arr[r][c] == 1:
        pass
    else:
        r += 1
    return r, c


for tc in range(1, T + 1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # x, y 좌표계 대신, r,c 로 행렬 성분으로 계산
    r, c = 99, 0
    for j in range(100):
        if arr[r][j] == 2:
            c = j
            break

    while r > 0:
        # 좌 탐색
        if 1 <= c < 100 and arr[r][c-1] == 1:
            r, c = turn_left_and_go((r, c), arr)
            #print(f"좌탐색 후 r,c are {r},{c}")
            # 전진
            r, c = go_upward_1cell((r, c), arr)
            #print(f"전진 후 r,c are {r},{c}")

        # 우 탐색
        elif 0 <= c <99 and arr[r][c+1] == 1:

            r, c = turn_right_and_go((r, c), arr)
            #print(f"우탐색 후 r,c are {r},{c}")
            # 전진
            r, c = go_upward_1cell((r, c), arr)
            #print(f"전진 후 r,c are {r},{c}")

        # 좌, 우측 모두 못간다면 위로 올라가기
        else:
            r, c = go_upward_1cell((r, c), arr)
            #print(f"전진 후 r,c are {r},{c}")
    print(f"#{tc} {c}")
