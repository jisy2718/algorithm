def select_loc(i):
    global result
    if i == N:
        result += 1
        return
    else:
        for j in range(N):
            # j가 유망한 곳이라면
            if used_col[j] == 0 and used_diag1[i+j] == 0 and used_diag2[i-j+N-1] == 0:
                used_col[j] = 1
                used_diag1[i + j] = 1
                used_diag2[i - j + N - 1] = 1
                select_loc(i+1)
                used_col[j] = 0
                used_diag1[i + j] = 0
                used_diag2[i - j + N - 1] = 0


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    used_col = [0]*N
    used_diag1 = [0]*(2*N - 1)  # / 방향 대각선으로, (i,j)에 대해 i + j = 0, 1, ..., 2N-2
    used_diag2 = [0]*(2*N - 1)  # \ 방향 대각선으로, (i,j)에 대해, i - j = -(N-1), -(N-2), ... 0, 1, ..., N-1
                                # 따라서 i - j + N -1 = 0, 1, 2, ... , N-1
    result = 0
    select_loc(0)
    print(f"#{tc} {result}")




