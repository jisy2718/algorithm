def find_prob(r,cur_prob):

    global max_prob
    global used_col
    # 마지막줄까지 확률계산한 경우
    if r == N:
        if max_prob < cur_prob:
            max_prob = cur_prob

    else:
        if cur_prob > max_prob: # promising
            for c in range(N):
                if used_col[c] == 0:
                    used_col[c] = 1  # c열 사용해서 함수 다시 실행
                    find_prob(r+1,cur_prob*arr[r][c]/100)
                    used_col[c] = 0  # c열 사용하지 않은 채로, 다음 loop 에서 이용할 c 찾기


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    max_prob = 0
    used_col = [0]*N
    find_prob(r=0,cur_prob=1)

    print(f"#{tc} {round(max_prob*100,6):.6f}")

