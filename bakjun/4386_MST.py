# 별자리 만들기

N = int(input())

coor = []
for _ in range(N):
    x, y = map(float, input().split())
    coor.append([x,y])


def dist(coor1, coor2):
    x1, y1 = coor1
    x2, y2 = coor2
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

arr = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(i,N):
        arr[i][j] = arr[j][i] =  dist(coor[i], coor[j])




def prim(start):
    MST = [0] * N
    MST[start] = 1
    w_sum = 0
    for _ in range(1,N):
        min_idx = 0
        min_val = 0xfffffffff
        for i in range(N):
            if MST[i] == 1:
                for j in range(N):
                    if min_val > arr[i][j] and MST[j]==0:
                        min_val = arr[i][j]
                        min_idx = j
        MST[min_idx] = 1
        w_sum += min_val

    print(w_sum)

prim(1)