
# 1. input
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 2. min_value 초기화
    min_sum = 0
    for i in range(N):
        min_sum += arr[i][i]

    used_row_col = [[None, None]] * N


    def partial_sum(row_idx, arr, N):
        global used_row_col
        global min_sum
        # 부분합을 찾은 것
        if row_idx == N:
            cur_sum = 0
            for c in range(N):
                cur_sum += arr[used_row_col[c][0], c]  # 해당 행의, i 열이 사용됨
            print(f'cursum is {cur_sum}')
            if min_sum > cur_sum:
                min_sum = cur_sum
            return

        for c in range(N):
            print(f'c is {c} row_idx is {row_idx}')
            if used_row_col[c][1] != 1: # c열이 사용되지 않았다면
                used_row_col[c][1] = 1  # c열 사용
                used_row_col[c][0] = row_idx  # row_idx 행에서 c열 사용
                print(used_row_col)
                print(f'---row idx is {row_idx}')
                partial_sum(row_idx + 1, arr, N)  # 다음 행에 대해서 진행

                # 이전으로 되돌리기
                used_row_col[c][1] = None  # c열 사용 취소
                used_row_col[c][0] = None  # row_idx 행에서 c열 사용 취소
                print(f"after none {used_row_col}")

    partial_sum(0, arr, N)

    print(f"#{tc} {min_sum}")