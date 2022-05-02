
N = int(input())
#  a, b, c, d 가 위치
#  거리 a--2--b--3--c--1--d
#  가격 5     2     4       d에서의 가격은 필요없음
distance = list(map(int,input().split()))
price = list(map(int,input().split()))[:-1]


# 현재 위치의 price 보다 싼 price가 있는 위치까지 갈만큼 넣으면 됨

cur_loc = 0
next_loc = 0
total_cost = 0
# 길이가 N-1 인 배열탐색하므로 마지막까지 탐색 후 값이 N-1 되면 다 탐색한 것
while cur_loc < N-1:
    cur_price = price[cur_loc]
    while next_loc < N-1 and price[next_loc] >= cur_price:
        next_loc += 1

    move = 0 # 이동해야 하는 거리
    for loc in range(cur_loc, next_loc): # 현재위치에서 next_loc 까지 갈 기름 넣으면 됨
        move +=  distance[loc]

    total_cost += move*price[cur_loc] # 현재 위치에서 넣어야 하는 기름의 양과 가격

    # 이동 시작
    cur_loc = next_loc  # 이동 완료

print(total_cost)