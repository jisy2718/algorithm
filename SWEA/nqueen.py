def nqueen(cur_r):
    global result
    r = cur_r
    if r == N:
        result += 1

    else:
        for c in range(N):
            cr, cc = r, c
            if promising(cr, cc): # cr, cc가 유망한지 탐색
                col[cc] = 1
                right_diag[N - 1 + (cr - cc)] = 1
                left_diag[cr + cc] = 1
                nqueen(cr + 1)
                col[cc] = 0
                right_diag[N - 1 + (cr - cc)] = 0
                left_diag[cr + cc] = 0
    return


def promising(cr, cc):
    if col[cc] == 0 and right_diag[N - 1 + (cr - cc)] == 0 and left_diag[cr + cc] == 0:
        return True
    else:
        return False

for i in range(1,16):
    N = i


    arr = [[0]*N for _ in range(N)]
    col = [0]*N
    right_diag = [0]*(2*N-1) # \ 방향 대각선 r-c = -(N-1), -(N-2) , ... 0, 1, ... N-2, N-1    \\\\\ + N -1 = -> 0, 1, 2 ,, 2N-1
    left_diag = [0]*(2*N-1) # / 방향 대각선 r+c = 0, 1, 2, 3, ... , 2N-2 //
    result = 0
    nqueen(0)
    print(f"N : {N}, result : {result}")