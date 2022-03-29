import sys
sys.stdin = open('4366_input.txt')
#--------------------------------------1번풀이 시작---------------------------------------------------
#
# def binary_to_decimal(binary:list):
#     result = 0
#     i = 0
#     while binary:
#         result += int(binary[-1])*2**i
#         i += 1
#         binary = binary[:-1]
#     return result
#
# def ternary_to_decimal(ternary:list):
#     result = 0
#     i = 0
#     while ternary:
#         result += int(ternary[-1])*3**i
#         i += 1
#         ternary = ternary[:-1]
#     return result
#
#
# T = int(input())
# for tc in range(1,T+1):
#     binary = list(input())
#     ternary = list(input())
#     result = 0
#     flag = False # 답을 못찾은 상황
#     # binary 모든 경우 변환하고, ternary 모든 경우 변환해서 저장 / 중복원소 생기면 그게 답
#     result_set = set()
#     for i in range(len(binary)):
#         modified_binary = binary.copy()
#         if binary[i] == '0':
#             modified_binary[i] = '1'
#         else:
#             modified_binary[i] = '0'
#         result_set.add(binary_to_decimal(modified_binary))
#
#     for j in range(len(ternary)):
#         modified_ternary = ternary.copy()
#         if ternary[j] == '0':
#             nums = ['1','2']
#             for k in range(2):
#                 num = nums[k]
#                 modified_ternary[j] = num
#                 decimal = ternary_to_decimal(modified_ternary)
#                 if decimal in result_set:
#                     result = decimal
#                     flag = True
#                     break
#                 else:
#                     result_set.add(decimal)
#             if flag == True:
#                 break
#
#         elif ternary[j] == '1':
#             nums = ['0','2']
#             for k in range(2):
#                 num = nums[k]
#                 modified_ternary[j] = num
#                 decimal = ternary_to_decimal(modified_ternary)
#                 if decimal in result_set:
#                     result = decimal
#                     flag = True
#                     break
#                 else:
#                     result_set.add(decimal)
#             if flag == True:
#                 break
#
#         elif ternary[j] == '2':
#             nums = ['1','0']
#             for k in range(2):
#                 num = nums[k]
#                 modified_ternary[j] = num
#                 decimal = ternary_to_decimal(modified_ternary)
#                 if decimal in result_set:
#                     result = decimal
#                     flag = True
#                     break
#                 else:
#                     result_set.add(decimal)
#             if flag == True:
#                 break
#     print(f"#{tc} {result}")

#--------------------------------------1번풀이 끝--------------------------------------------


#---------------------------2번 풀이 시작------------------------------------------
# 지금 binary를 모든 경우의 수에 따라 바꾸는 것이 구현 안되어 있음.
from typing import List

def binary_to_ternary(binary:List[int]):
    # 십진수로 바꾸기
    decimal = 0
    for i in range(-1,-len(binary)-1,-1):
        decimal += binary[i]*2**(-i)

    # 삼진수로 바꾸기
    ternary = []
    tmp = decimal
    while tmp:
        ternary.append(tmp%3)
        tmp//= 3
    ternary = ternary[::-1]


    return ternary, decimal

def solve(btt,ternary):
    cnt = 0
    for i in range(len(btt)):
        if btt[i] != ternary[i]:
            cnt += 1

    if cnt == 1:
        return True
    else:
        return False



T = int(input())
for tc in range(1,T+1):
    binary = list(map(int,input()))
    ternary = list(map(int,input()))
    print(binary,ternary)
    btt, decimal = binary_to_ternary(binary)  # 3진수 값과, 10진수 값 반환
    print(btt, ternary)
    # ternary 와 btt 비교해서 1자리만 다르면 ok
    if solve(btt,ternary):
        print(f'#{tc} {decimal}')
