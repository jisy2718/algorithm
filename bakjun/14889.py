# SWEA 4012 요리사문제와 유사

import sys
input = sys.stdin.readline
N = int(input())
arr = [[0]*(N+1)] + [[0] + list(map(int,input().split())) for _ in range(N)]
a = list(range(1,N+1))

#-------------------------------------------------------------------------------
# def perm(idx):
#     if idx == N//2:
#         print(p)
#         if p[:N//2] not in results:
#             results.append(p[:N//2]) # 가능한 순열 저장
#
#     else:
#         for i in range(N):
#             if used[i] == 0:
#                 used[i] = 1
#                 print(f"idx is {idx}, i is {i}")
#                 print(f"p len is {len(p)}")
#                 p[idx] = a[i]
#                 perm(idx+1)
#                 used[i] = 0
# used = [0]*N
# perm(0)


# # 3. 기본형
# def nCr(n,r,s): # n개에서 r개를 고르는 조합, s: 선택할 수 있는 구간의 시작
#     if r == 0: # 더 이상 고를 것이 없다
#         results.append(comb)
#     else:
#         for i in range(s, n-(r-1)):
#             comb[r-1] = a[i]
#             nCr(n,r-1,i+1)
#
#     return
#     comb = [0]*(N//2)
# results = []
# nCr(N,N//2,0)
# p = [0]*N
#
# print(results)

#
# def combination(selected, idx, cnt):
#     if cnt == N//2:
#         result = []
#         for i in range(N):
#             if selected[i] !=0:
#                 result.append(a[i])
#         results.append(result)
#
#     if idx >= N:
#         return
#
#     selected[idx] = 1
#     combination(selected, idx+1, cnt+1)
#     selected[idx] = 0
#     combination(selected, idx+1, cnt)
#
# results = []
# selected = [0]*N
# combination(selected, 0, 0)


# ------------------------------------
# def nCr(n,r,s,k): # n개에서 r개를 고르는 조합, s: 선택구간 시작, k:고른 개수
#     # print(f"k is {k} comb is {comb} results is {results}")
#     if k == r:
#         # print(comb)
#         results.append(set(comb[:]))
#         # print(results)
#     else:
#         for i in range(s, n-r+k+1):
#             comb[k] = a[i]
#             # print(comb, k)
#             nCr(n,r,i+1,k+1)
#     return
# n = N
# r = N//2
# a = [i for i in range(1,n+1)]
# comb = [0]*r
# results = []
# nCr(n,r,0,0)
#
# # print(results)
#
#
# #---------------------------------
#
#
#
#
# def find_complement(L):
#
#     temp = list(range(1,N+1))
#     for num in L:
#         temp.remove(num)
#     return temp
#
# cur_min = 10**8
#
# for subset in results:
#     c1 = subset
#     # print(f"c1 is {c1}")
#     c2 = find_complement(c1)
#     # print(c1, c2)
#
#     n1 = n2 =0
#
#     for i in range(1,N):
#         for j in range(i+1,N+1):
#             if i in c1 and j in c1:
#                 n1 += arr[i][j] + arr[j][i]
#
#             if i in c2 and j in c2:
#                 n2 += arr[i][j] + arr[j][i]
#     # print(n1, n2)
#     if abs(n1-n2) < cur_min:
#         cur_min = abs(n1-n2)
#
#
# print(cur_min)

#-------------------------------------------------------------------------------------
def nCr(n,r,s,k): # n개에서 r개를 고르는 조합, s: 선택구간 시작, k:고른 개수
    # print(f"k is {k} comb is {comb} results is {results}")
    if k == r:
        # print(comb)
        results.append(set(comb[:]))
        # print(results)
    else:
        for i in range(s, n-r+k+1):
            comb[k] = a[i]
            # print(comb, k)
            nCr(n,r,i+1,k+1)
    return
n = N
r = N//2
a = [i for i in range(1,n+1)]
comb = [0]*r
results = []
nCr(n,r,0,0)

# print(results)


#---------------------------------
cur_min = 10**8
for c1 in results:
    c2 = set(range(1,N+1)) - c1
    c1 = list(c1)
    c2 = list(c2)
    n1 = n2 =0

    for i in range(N//2-1):
        for j in range(i,N//2):
            n1 += arr[c1[i]][c1[j]]
            n1 += arr[c1[j]][c1[i]]

            n2 += arr[c2[i]][c2[j]]
            n2 += arr[c2[j]][c2[i]]


    if abs(n1-n2) < cur_min:
        cur_min = abs(n1-n2)


print(cur_min)