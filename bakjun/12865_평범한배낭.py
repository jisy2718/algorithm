# # -------------------------------------------DP 이용-------------------------------
# N, K = map(int,input().split())
#
#
# items = {} # {weight : value}
# for _ in range(N):
#     w, v = map(int,input().split())
#     if w in items:
#         items[w].append(v)
#
#     else:
#         items[w] = [v]
#
# for w in items:
#     items[w].sort(reverse=True)
#
#
# s = [0]*(K+1)
#
# # L의 무게에서 얻을 수 있는 최대 가치는, 모든 item 1,2,3,...,N에 대해서, 각 무게 w1, ... ,wN에 대해서
# # max( L-w_i 무게에서의 최대 가치 + item i 의 가치(==v_i) )
#
# for L in range(1,K+1):
#     for w in sorted(items): #[key값들의 list 정렬]
#         if 0 <= L - w and items[w]:
#             cur_value = s[L-w] + items[w][0]
#             if cur_value > s[L]:
#                 s[L] = cur_value
#                 items[w].pop(0)
# print(s)
#
# print(s[K])




# # -------------------------------------------부분집합-------------------------------
# import sys
# input = sys.stdin.readline
#
# N, K = map(int,input().split())
# items = [] # {weight : value}
# for _ in range(N):
#     w, v = map(int,input().split())
#     item = {w:v}
#     items.append(item)
#
# used = [0]*N
# p = [0]*N
# max_value = 0
# for i in range(1<<N):  # 전체 부분집합
#     # 부분집합 생성
#     for j in range(N):  # j번째 자리가 1인지아닌지
#         if i & (1<<j):
#             used[j] = 1
#
#     # 부분집합에 따른 가치 계산
#     cur_weight = 0
#     cur_value = 0
#     for j in range(N):
#         if used[j] == 1:
#             item = items[j]
#             wv = list(item.items())  # [(w,v)]
#             w, v = wv[0]
#             cur_weight = cur_weight+w
#             if cur_weight <= K:
#                 cur_value += v
#             else:
#                 break
#
#     if cur_value > max_value:
#         max_value = cur_value
#
#
#
#     # 부분집합 초기화
#     for j in range(N):
#         used[j] = 0
#
#
# print(max_value)




# # -------------------------------------------DP 이용-------------------------------
# N, K = map(int,input().split())
#
#
# items = [] # (weight,value)
# for _ in range(N):
#     w, v = map(int,input().split())
#     items.append((w,v))
#
# items.sort() # 무게가 가벼운 순서대로 정렬
#
# # 첫행 : 무게 / 둘째행 : 사용한 것
# s = [[0]*(K+1) ] + [[]]
# for _ in range(K+1):
#     lst = []
#     s[1].append(lst)
#
# # for row in s:
# #     print(row)
#
#
#
# # L의 무게에서 얻을 수 있는 최대 가치는, 모든 item 1,2,3,...,N에 대해서, 각 무게 w1, ... ,wN에 대해서
# # max( L-w_i 무게에서의 최대 가치 + item i 의 가치(==v_i) )
#
# for L in range(1,K+1):
#     cur_item = None
#     for item in items:  # 무게가 작은 item부터 진행
#         w, v = item
#         if 0 <= L - w :
#             # 사용했던 것이라면 넘어가기
#             for used_item in s[1][L-w]:
#                 if item == used_item:
#                     break
#             # 사용하지 않았던 것이라면 사용해보기
#             else:
#                 cur_value = s[0][L-w] + v
#                 if cur_value > s[0][L]:
#                     s[0][L] = cur_value
#                     cur_item = item
#
#     if cur_item != None:
#         s[1][L].append(cur_item)
#
# print(s[0][K])
#

# -------------------------------------------DP 이용-------------------------------
N, K = map(int,input().split())


items = [] # (weight,value)
for _ in range(N):
    w, v = map(int,input().split())
    items.append((w,v))


# 첫행 : 무게 / 둘째행 : 사용한 것
s = [0]*(K+1)




# L의 무게에서 얻을 수 있는 최대 가치는, 모든 item 1,2,3,...,N에 대해서, 각 무게 w1, ... ,wN에 대해서
# max( L-w_i 무게에서의 최대 가치 + item i 의 가치(==v_i) )

for w, v in items:
    # print(w,v)
    for w_to_K in range(K,w-1,-1): # 뒤에서부터 넣어야 함. 앞에서 부터 넣으면, 아래 max에서서 넣은 값을 또 이용게 됨
        # print(w_to_K)
        s[w_to_K] = max(s[w_to_K], s[w_to_K-w]+v) # 물건을 넣느냐 / 넣지 않느냐

print(s[K])

