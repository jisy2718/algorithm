#https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AX7cgLH6Z7QDFAS2&contestProbId=AV14ABYKADACFAYh&probBoxId=AX77LjUqEbgDFARO+&type=PROBLEM&problemBoxTitle=220215_%EC%8B%A4%EC%8A%B5%EB%B0%8F%EA%B3%BC%EC%A0%9C&problemBoxCnt=++5+

# 매 칸 이동하는 것을 반복문으로 처리

# 반복문 1번에 1칸 이동
import sys
sys.stdin = open('hw_0215_input.txt')


T = 10
for t in range(T):
    tc = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    # for row in ladder:
    #     print(row)
    # if t == 0:
    #     break

    # 사다리타기 시작
    # 0행을 검사를 해서, 시작점이라면 (1이라면) 시작
    dr = [1,0,0] # 아래, 오른, 왼쪽에 대한 row의 변화량
    dc = [0,1,-1]
    for i in range(100):
        if ladder[0][i]: # 시작점 찾음
            # 현재 위치를 r, c로 저장
            # 움직이는 방향 3개 설정 : 0:아래, 1:오른쪽, 2:왼쪽
            # 변화량 배열
            # 현재 위치 + 움직이는 방향에 대한 더하기
            # 방향을 바꿔야 하는 경우 생기면 방향 바꾸기
            # 움직이는 방향 : 아래쪽 > 좌 or 우 갈 수 있는 길이 있을 때,
            #             : 좌 or 우 > 아래쪽으로 갈 수 있는 길이 있을 때
            # r 이 99라면 멈춰

            r,c = 0, i # 현재 위치
            d = 0 # 현재 방향은 아래쪽
            while r < 99: # r이 99가 되면 멈춤 ( 끝에 도달 )
                # 움직이기 전에 방향을 바꾸는 경우가 있는지 검사
                # 현재 움직이고 있는 방향에 따라서 방향을 바꾸는 검사가 다름
                if d == 0: # 아래 방향으로 움직이고 있었으면
                    # 좌 or 우측 검사 << 양쪽에 0이 있으면 편하다
                    if c > 0 and ladder[r][c-1]: # 좌측 검사
                        d = 2

                    elif c < 99 and ladder[r][c+1]: # 우측 검사
                        d = 1

                else: # 오른쪽, 왼쪽으로 갈 땐 아래쪽 검사
                    if ladder[r+1][c] == 1:
                        d = 0
                # 현재 움직이는 방향에 대해서 변화량 더하기
                r += dr[d]
                c += dc[d]
            # r 이 99가 되면서, 반복이 끝난 시점에서 ladder[r][c] = 2라면,
            #
            if ladder[r][c] == 2:
                return i









