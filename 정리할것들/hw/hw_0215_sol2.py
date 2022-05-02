import sys
# 표준 입력 경로 변경
sys.stdin = open("hw_0215_input.txt", 'r')



T = 10
for tc in range(1, T + 1):
    tc = int(input())
    # input
    arr = [list(map(int, input().split())) for _ in range(100)]

    # x, y 좌표계 대신, r,c 로 행렬 성분으로 계산
    # 2의 위치 찾기
    r, c = 99, 0
    for j in range(100):
        if arr[r][j] == 2:
            c = j
            break
    # 이동하기
    while r > 0:
        # 일단 1칸 전진 (좌측, 우측 으로 이동 불가 상태임 )
        r -= 1
        # if 좌측 살핀 후, 1이라면 좌측 끝까지 이동
        if 1 <= c < 100 and arr[r][c-1] == 1:
            while 1 <= c < 100 and arr[r][c-1] == 1:
                c -= 1
        # elif 우측 살핀 후, 1이라면 우측 끝까지 이동
        elif 0 <= c < 99 and arr[r][c+1] == 1:
            while 0 <= c < 99 and arr[r][c+1] == 1:
                c += 1


    print(f"#{tc} {c}")