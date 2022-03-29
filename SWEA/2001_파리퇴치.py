import sys
sys.stdin = open('2001_input.txt')


T = int(input())

for tc in range(1,T+1):
    N, M = list(map(int,input().split()))

    arr = [list(map(int,input().split())) for _ in range(N)]
    max_val = 0
    for r in range(N-M+1): # 대각선으로 생각해보면 N - M + 1, N - M + 1 회 접근
        for c in range(N-M+1):
            cnt = 0 # 현재 기준을 좌측상단 칸으로 보고  MxM 의 합 초기화
            for i in range(M):
                for j in range(M):
                    cnt += arr[r+i][c+j]
            if max_val < cnt: # 비교
                max_val = cnt
    print(f"#{tc} {max_val}")
