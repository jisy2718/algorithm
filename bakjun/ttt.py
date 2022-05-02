import sys
input = sys.stdin.readline

N = int(input())

arr_x = [list(input()) for _ in range(N)]  # 색약 x
arr_o = [[0]*N for _ in range(N)]          # 색약 o
for i in range(N):
    for j in range(N):
        if arr_x[i][j] == 'B':
            arr_o[i][j] = arr_x[i][j]
        else:
            arr_o[i][j] = 'G'


def find_set(a,make_set):
    x, y = a
    if make_set[x][y] == [x,y]:
        return [x,y]
    else:
        return find_set(make_set[x][y],make_set)

def union(a,b,make_set):
    root_a = find_set(a,make_set)
    root_b = find_set(b,make_set)
    make_set[root_b[0]][root_b[1]] = root_a
    return



make_set_x = [ [ [i,j] for j in range(N)] for i in range(N) ] # 1. 색약 x
make_set_o = [ [ [i,j] for j in range(N)] for i in range(N) ] # 2. 색약 o

# 자신의 왼쪽 & 위쪽과 비교해서 union 하기
for i in range(N):
    for j in range(N):
        # 위쪽
        if 0 <= i-1 < N:
            if arr_x[i-1][j] == arr_x[i][j]:
                union([i-1,j],[i,j],make_set_x)
            if arr_o[i-1][j] == arr_o[i][j]:
                union([i-1,j],[i,j],make_set_o)

        # 왼쪽
        if 0 <= j-1 < N:
            if arr_x[i][j-1] == arr_x[i][j]:
                union([i,j-1],[i,j],make_set_x)
            if arr_o[i][j-1] == arr_o[i][j]:
                union([i,j-1],[i,j],make_set_o)

count_x = 0
count_o = 0
for i in range(N):
    for j in range(N):
        if make_set_x[i][j] == [i,j]:
            count_x += 1
        if make_set_o[i][j] == [i,j]:
            count_o += 1

print(count_x, count_o)