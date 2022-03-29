# 달팽이 정렬
# N = 5
# arr = [[0]*N for _ in range(N)]
#
# # 우 하 좌 상
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
#
# # 0, 1, 2, 3 : 우 하 좌 상
# direction = 0
#
# # 시작점 / r,c 는 현재 위치
# r = c = 0
# num = 1
#
# # N * N 행렬에 1부터 N*N 까지 정수를 하나씩 넣기
# # 숫자를 행렬에 다 넣을때까지 계속 반복
# # 이동하고 숫자넣기
#
# while num <= N*N:
#     # 정상 범위이고, 다른 숫자 없으면 숫자 할당
#     if 0 <= r < N and 0 <= c < N and not arr[r][c] :
#         arr[r][c] = num
#
#         num += 1
#     else:
#         # 정상범위가 아니므로 이동 방향을 바꿔야 함
#         # 현재 r,c는 범위를 벗어난 상태
#         # 정상범위로 돌아옴
#         r -= dr[direction]
#         c -= dc[direction]
#
#         # 지금 가는 방향으로 계속가면 또 범위 벗어남... 방향 전환
#         direction = ( direction + 1) % 4
#
#     r += dr[direction]
#     c += dc[direction]
#
#     for row in arr:
#         print(row)
#     print("-----------------------")
#
# num = 1
# while arr[r + dr[direction]][c+dc[direction]] not in used:
#     arr[r + dr[direction]][c + dc[direction]] = num
#     used.add(num)
#     # 현재 방향으로 진행가능하면 계속 진행
#


# my sol 미완성
N = 5
arr = [[0]*N for _ in range(N)]

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 0, 1, 2, 3 : 우 하 좌 상
direction = 0

# 시작점 / r,c 는 현재 위치
r = c = 0
num = 1
used = set()

# 사용되지 않았다면 추가
while num <= 25:


    # 다음 범위가 정상 범위이고, 사용하지 않은 것인 경우 while 문으로 돌아감
    if 0 <= r < N and 0 <= c < N and arr[r][c] not in used:
        arr[r][c] = num
        used.add(num)
        num += 1

        # 다음 범위
        r += dr[direction]
        c += dr[direction]

    else:
        # 이전으로 돌아가 방향 틀기
        r -= dr[direction]
        c -= dc[direction]
        direction = ( direction + 1) % 4

        # 전진
        r += dr[direction]
        c += dc[direction]

print(arr)