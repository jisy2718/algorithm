import sys
input = sys.stdin.readline


#-----------------------------------틀린풀이------------------------------------------------
# N = int(input())
# arr = list(map(int,input().split())) # 길이 N
# cal = list(map(int,input().split()))  # 0 : +, 1: - , 2 : x, 3 : //
#
# # 음수는 양수로 바꾼 뒤 나누고 다시 - 붙이기
#
# # 연산 가능한 경우의 수 모두 찾아서 완전탐색
# # 순열의 수를 구해보자
# a = [0]*cal[0] + [1]*cal[1] + [2]*cal[2] + [3]*cal[3]   # 길이 N-1
# used = [0]*(N-1)  # N-1 개
# perms = set()
# p = [0]*(N-1)
# def perm(idx):
#     if idx == N-1:
#         perms.add(tuple(p)) # 가능한 순열 저장
#         # print(f"pis {p}")
#
#     else:
#         for i in range(N-1):
#             if used[i] == 0:
#                 used[i] = 1
#                 p[idx] = a[i]
#                 perm(idx+1)
#                 used[i] = 0
#
# def calcul(a1,a2,oper):
#     if oper == 0:
#         return a1 + a2
#     elif oper == 1:
#         return a1 - a2
#     elif oper == 2:
#         return a1*a2
#     elif oper == 3:
#         if a1<0:
#             temp = -a1
#             return -(temp//a2)
#         else:
#             return a1//a2
#
# perm(0)
#
# cur_min = 0xffffff
# cur_max = -0xffffff
#
# import copy
# for per in perms:
#     temp = copy.deepcopy(arr)
#     for i in range(N-1):
#         temp[i+1] = calcul(temp[i],temp[i+1],per[i])
#
#     if cur_min > temp[N-1]:
#         cur_min = temp[N-1]
#     if cur_max < temp[N-1]:
#         cur_max = temp[N-1]
#
# print(cur_max)
# print(cur_min)
#---------------------------------------------------------------------------------------

#---------------DFS 이용----------------------------------------------------------------

N = int(input())
arr = list(map(int,input().split()))
oper = list(map(int,input().split()))

def dfs(oper, cur_val,idx):
    global cur_min
    global cur_max
    if idx == N:

        if cur_val > cur_max:
            cur_max = cur_val
        if cur_val < cur_min:
            cur_min = cur_val
        return

    else:
        if oper[0]:
            oper[0] -= 1
            dfs(oper, cur_val+arr[idx], idx+1)
            oper[0] += 1

        if oper[1]:
            oper[1] -= 1
            dfs(oper,cur_val-arr[idx], idx+1)
            oper[1] += 1

        if oper[2]:
            oper[2] -= 1
            dfs(oper,cur_val*arr[idx], idx+1)
            oper[2] += 1

        if oper[3]:
            oper[3] -=1
            if cur_val <0:
                cur_val = -cur_val
                dfs(oper, -(cur_val//arr[idx]), idx+1)

            else:
                dfs(oper, cur_val//arr[idx], idx + 1)

            oper[3] += 1
    return

cur_min = 0xfffff
cur_max = -0xfffff
dfs(oper,arr[0],1)
print(cur_max)
print(cur_min)



