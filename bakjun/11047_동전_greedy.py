

N, K = map(int,input().split())

moneys = []
for _ in range(N):
    money = int(input())
    moneys.append(money)

i = N-1
result = 0
while K>0:
    if K >= moneys[i]:
        result += K//moneys[i]
        K = K % moneys[i]

    i -= 1

print(result)

















# ----------------------답1 오답-------------------------------------------
#
# N, K = map(int,input().split())
#
# moneys = []
# for _ in range(N):
#     money = int(input())
#     moneys.append(money)
#
#
# # greedy가 가능한 경우 찾기
# for i in range(N-1,0,-1):
#     if moneys[i]% moneys[i-1] !=0:
#         break
#
# # greedy가 가능한 경우
# else:
#     result = 0
#     i = N-1
#     while K !=0:
#         if K > moneys[i] :
#             while K >= moneys[i]:
#                 K -= moneys[i]
#                 result += 1
#         i -= 1
#
#     print(result)



# # greedy가 불가능한 경우--
# def dfs(cur_K, result):
#     global min_result
#     # print(min_result)
#     if cur_K == 0:
#         if min_result > result:
#             min_result = result
#     else:
#         for i in range(N-1,-1,-1):
#             if cur_K - moneys[i] >= 0:
#                 cnt = cur_K // moneys[i]
#                 cur_K = cur_K % moneys[i]
#                 dfs(cur_K , result+cnt)
#
#
# min_result = 0xfffff
# dfs(K, 0)
# print(min_result)
# ---------------------------------------------------------------------------



