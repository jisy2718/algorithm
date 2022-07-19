# M개의 주사위 전체의 합을 구하는 문제인줄 알고, 푼 풀이
#
# M = int(input())
#
# # 전체 input 받기
# arr = [[],[]]
# for _ in range(M):
#     n, s = map(int,input().split())
#     arr[0].append(n)
#     arr[1].append(s)
#
#
# # 최대공약수 구하기
# def gcd(L:list):
#     tmp = L.copy()
#     result = 1
#     max_num = max(tmp)
#
#     i = 2
#     while i < max_num:
#         for j in range(M):
#             if tmp[j] % i != 0:
#                 i += 1
#                 break
#         else:
#             result *= i
#             for j in range(M):
#                 tmp[j] = tmp[j]//i
#         # print('gcd i is', i)
#         # print('result is', result)
#
#     return result
#
#
# # 최소공배수 구하기
# def lcm(L:list):
#     tmp = gcd(L)
#     tmpL = L.copy()
#
#     for j in range(M):
#         tmpL[j] = tmpL[j]//tmp
#
#
#     for j in range(M):
#         tmp = tmp*tmpL[j]
#
#
#     return tmp
#
# # 전체 합 구하기
# LCM = lcm(arr[0])
#
# for j in range(M):
#
#     n = arr[0][j]
#     multi = LCM//n
#     arr[1][j] *= multi
#
# top = sum(arr[1])
#
# bottom = LCM
#
#
#
# # 기약분수 만들기
# GCD = gcd([top,bottom])
#
# a = top // GCD
# b = bottom // GCD
# print(a,b, GCD)
#
# # 모듈러 역원 찾기
# X = 1000000007
# # a를 b번 제곱한 것을 c로나눈 나머지
# def f(a,b,c):
#     if b == 1:
#         return a%c
#
#     reduced = f(a,b//2,c)
#
#     if b%2==0:
#         return (reduced**2)%c
#     else:
#         return ((reduced**2)*a)%c
#
# result  = f(b, X-2, X)
# result *= a
# result %= X
# print(result)
#
#

from math import gcd
# M개 주사위 각각의 기대값을 나타내는 것이 원하는 답
M = int(input())

# 전체 input 받기
arr = [[],[]]
for _ in range(M):
    n, s = map(int,input().split())
    arr[0].append(n)
    arr[1].append(s)

#
# # 최대공약수 구하기
# def gcd(L:list):
#     tmp = L.copy()
#     result = 1
#     min_num = min(tmp)
#
#     i = 2
#     while i <= min_num:
#         for j in range(len(L)):
#             if tmp[j] % i != 0:
#                 i += 1
#                 break
#         else:
#             result *= i
#             for j in range(len(L)):
#                 tmp[j] = tmp[j]//i
#         # print('gcd i is', i)
#         # print('result is', result)
#
#     return result

# a를 b번 제곱한 것을 c로나눈 나머지
def f(a,b,c):
    if b == 1:
        return a%c

    reduced = f(a,b//2,c)

    if b%2==0:
        return (reduced**2)%c
    else:
        return ((reduced**2)*a)%c

X = 1000000007
answer = 0
for i in range(M):
    n = arr[0][i]
    s = arr[1][i]

    # 기약분수 만들기
    GCD = gcd(n,s)
    # print(GCD,n,s)

    a = s // GCD
    b = n // GCD
    # print(GCD,b,a)

    # 모듈러 역원 찾기



    result  = f(b, X-2, X)  # b의 역원의 모듈러 X값
    result *= a    # ab^-1 의 모듈러 X값

    answer += result
    answer %= X
print(answer)





