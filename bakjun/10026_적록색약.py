N = int(input())

arr = [list(input()) for _ in range(N)]


def find_set(a):
    x, y = a
    if make_set[x][y] == [x,y]:
        return [x,y]
    else:
        return find_set(make_set[x][y])

def union(a,b):
    root_a = find_set(a)
    root_b = find_set(b)
    make_set[root_b[0]][root_b[1]] = root_a
    return

# 1. 색약 x

make_set = [ [ [i,j] for j in range(N)] for i in range(N) ]

# 자신의 왼쪽 & 위쪽과 비교해서 union 하기
for i in range(N):
    for j in range(N):
        # 위쪽
        if 0 <= i-1 < N:
            if arr[i-1][j] == arr[i][j]:
                union([i-1,j],[i,j])

        # 왼쪽
        if 0 <= j-1 < N:
            if arr[i][j-1] == arr[i][j]:
                union([i,j-1],[i,j])

count1 = 0
for i in range(N):
    for j in range(N):
        if make_set[i][j] == [i,j]:
            count1 += 1



# 2. 색약 o

make_set = [ [ [i,j] for j in range(N)] for i in range(N) ]

# 자신의 왼쪽 & 위쪽과 비교해서 union 하기
for i in range(N):
    for j in range(N):
        # 위쪽
        if 0 <= i - 1 < N:
            if arr[i][j] in ['R','G']:
                if arr[i - 1][j] in ['R','G']:
                    union([i - 1, j], [i, j])
            else:
                if arr[i-1][j] == arr[i][j]:
                    union([i - 1, j], [i, j])


        # 왼쪽
        if 0 <= j - 1 < N:
            if arr[i][j] in ['R','G']:
                if arr[i][j-1] in ['R','G']:
                    union([i, j-1], [i, j])

            else:
                if arr[i][j - 1] == arr[i][j]:
                    union([i, j - 1], [i, j])

count2 = 0
for i in range(N):
    for j in range(N):
        if make_set[i][j] == [i, j]:
            count2 += 1

print(count1, count2)



