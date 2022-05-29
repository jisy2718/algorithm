# def lsm(M,N):
#     def gcd(M,N):
#         result = 1
#         cur = 2
#
#         while cur <= max(M,N):
#             while M % cur ==0 and N % cur ==0:
#                 result *= cur
#                 M //= cur
#                 N //= cur
#
#             cur += 1
#         return result
#
#     gcd_MN = gcd(M,N)
#     result = M*N*gcd_MN
#     return result
#
# import sys
# input = sys.stdin.readline
# T = int(input())
# for tc in range(T):
#     M, N, tx, ty = map(int,input().split())
#
#     # 1. x,y를 계속 변화시키기
#
#     # 2. 유효한 숫자인지 check
#
#     year = 1
#     x, y = 1, 1
#     flag = False
#
#     # max_year = lsm(M,N)
#
#     while True :
#         if x > M :
#             x %= M
#         if y > N:
#             y %= N
#         if tx == x and ty == y:
#             flag = True
#             break
#
#         # 이미 사용되었는데, 아직 true 아니면 만드는 것 불가능함.
#         if year > M*N:
#             flag = False
#             break
#
#         year += 1
#         x += 1
#         y += 1
#
#
#
#     if flag == False:
#         print(-1)
#     else:
#         print(year)
#----------------------------------------------------------------------------------------------
# def lsm(M,N):
#     def gcd(M,N):
#         result = 1
#         cur = 2
#
#         while cur <= max(M,N):
#             while M % cur ==0 and N % cur ==0:
#                 result *= cur
#                 M //= cur
#                 N //= cur
#
#             cur += 1
#         return result
#
#     gcd_MN = gcd(M,N)
#     result = M*N*gcd_MN
#     return result



# moduler 이용
import sys
input = sys.stdin.readline
T = int(input())
for tc in range(T):
    M, N, tx, ty = map(int,input().split())
    result = -1
    year1 = 0
    year2 = 0

    while (tx+ year1*M) <= M*N:
        if (tx+ year1*M) ==( ty + year2*N) :
            result = tx+ year1*M
            break
        elif (tx+ year1*M) < ( ty + year2*N) :
            year1 += 1

        else:
            year2 += 1


    print(result)

M, N = 8, 10
11
22
33
44
55
66
77
88
19
210
31: 11년
3 + 8 * 1 = 1 + 10 * 1
4
2
5
3: 13
년
5 + 8 * 1 = 3 + 10 * 1
6
4
7
5
8
6
1
7: 17 = 1 + 8 * 2 = 7 + 10 * 1

a
b: ??년
a + 8 * year1 = b + 10 * year2