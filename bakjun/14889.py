# SWEA 4012 요리사문제와 유사

#-------------------------------------------------------------------------------------#
# import sys
# input = sys.stdin.readline
# N = int(input())
# arr = [[0]*(N+1)] + [[0] + list(map(int,input().split())) for _ in range(N)]
# a = list(range(1,N+1))

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
# N = 5
# n = N
# r = N//2
# a = [i for i in range(1,n+1)]
# comb = [0]*r
# results = []
# nCr(n,r,0,0)
#
# print(results)

# cur_min = 10**8
# for c1 in results:
#     c2 = set(range(1,N+1)) - c1
#     c1 = list(c1)
#     c2 = list(c2)
#     n1 = n2 =0
#
#     for i in range(N//2-1):
#         for j in range(i,N//2):
#             n1 += arr[c1[i]][c1[j]]
#             n1 += arr[c1[j]][c1[i]]
#
#             n2 += arr[c2[i]][c2[j]]
#             n2 += arr[c2[j]][c2[i]]
#
#
#     if abs(n1-n2) < cur_min:
#         cur_min = abs(n1-n2)
#
#
# print(cur_min)

#-----------------------------2. dfs(tree구조)이용-----------------------------------------------------------------
def dfs(n,alst,blst):
    global gmin

    #-------------------- 나중에 돌려보고 적는 부분----------
    if len(alst) > N//2 or len(blst) > N//2: # 백트래킹
        return
    #-------------------------------------------------------

    if n == N:  # 종료조건
        if len(alst) == len(blst):
            asum = bsum = 0
            for i in range(N//2):
                for j in range(N//2):
                    asum += arr[alst[i]][alst[j]]
                    bsum += arr[blst[i]][blst[j]]

            if gmin > abs(asum-bsum):
                gmin = abs(asum-bsum)

        return

    else:
        dfs(n+1, alst+[n], blst)  # a에 포함시키는 경우
        dfs(n+1, alst, blst+[n])  # a에 포함 안시키는 경우



import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
gmin = 0xffffffff
dfs(0,[],[])
print(gmin)
