# 모든 집과 치킨집 사이의 거리를 구한 후,
# 치킨집 M개 선택했을 때의 최소거리를 계산

N, M = map(int,input().split())


arr = [list(map(int,input().split())) for _ in range(N)]

num_store = 0
num_house = 0
for r in range(N):
    for c in range(N):
        if arr[r][c]==2:
            num_store+=1
        elif arr[r][c] == 1:
            num_house +=1

dist = [[0]*num_house for _ in range(num_store)] # dist[store][house]

cur_house = 0
for r in range(N):
    for c in range(N):
        # 집이라면
        if arr[r][c] == 1:
            # 치킨집 찾기
            cur_store=0
            for rr in range(N):
                for cc in range(N):
                    if arr[rr][cc] == 2:
                        man = abs(rr-r) + abs(cc-c)
                        dist[cur_store][cur_house] = man
                        cur_store +=1

            cur_house +=1
            cur_sotre = 0

# for row in dist:
#     print(row)


# sotre를 M 개 조합하기
stores = list(range(num_store))
comb = [0]*M
min_dist = 0xfffffffffffff
def nCr(r,s):
    global min_dist
    if r == 0:
        # 치킨집 선정
        selected = []
        for m in comb:

            selected.append(dist[m])
        # for row in selected:
        #     print(row)
        selected = list(map(list,zip(*selected))) # selected[house][store]
        cur_min = 0
        # for row in selected:
        #     print(row)
        for n in range(num_house):
            cur_min += min(selected[n])
            if cur_min >= min_dist:
                break
        else:
            min_dist = cur_min




    else:
        for i in range(s, num_store-(r-1)):
            comb[r-1] = stores[i]
            # print('comb is',comb)
            nCr(r-1,i+1)

nCr(M,0)
print(min_dist)


