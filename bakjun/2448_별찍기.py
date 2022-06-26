#
#
# N = int(input())
# nrow = N
# N //= 3
# k = 0
# while N>1:
#     N//=2
#     k+=1
#
#
# # 각 라인 별 빈칸 개수
# total = 5 + 6*(2**k-1)
#
#
# # 첫 row 생략
# stars = [ [' ']*total for _ in range(nrow+1)]
#
#
#
# def make_star(r,c, front, back):
#     if r == N+1:
#         return
#
#     # 첫행
#     stars[r][c] = '*'
#
#     # 둘째 행
#     stars[r+1][c-1] = '*'
#     stars[r + 1][c + 1] = '*'
#
#     # 셋째 행
#     for i in range(-2,3):
#         stars[r + 2][c+i] = '*'
#
#
#     # 현재 세모의 위치가 맨뒤인지 맨 앞인지 파악
#     front_flag = False
#     back_flag = False
#     if front == True:
#         front_flag = True
#     if back == True:
#         back_flag = True
#
#
#     # 별 5개 짜리 행이 홀수 행일 경우 2개 씩 생성
#     if (r+2) % 2 == 1:
#         make_star(r+1,c-3,front_flag, False)
#         make_star(r+1, c+3, False, back_flag)
#
#     # 짝수행일 경우, front와 back 부분에서만 1개씩 생성
#     else:
#     make_star(r+1,c-1, True)



#-------------------------------------------------


N = int(input())
nrow = N
N //= 3
k = 0
while N > 1:
    N //= 2
    k += 1

# 각 라인 별 빈칸 개수
total = 5 + 6 * (2 ** k - 1)

stars = ["  *  ", " * * ", "*****"]


def make_tri(stars):
    L = len(stars)
    for i in range(L):
        # 아래에 새로운 삼각형 만들기
        stars.append(stars[i]+' ' + stars[i])

        # 기존의 삼각형 여백 넣어주기  : 새로 생길 줄 수 만큼 밀어줘야 함. 새로생길 줄 수는 기존의 길이 L
        stars[i] = ' '*L + stars[i] + ' '*L





for _ in range(k):
    make_tri(stars)

for row in stars:
    print(row)
