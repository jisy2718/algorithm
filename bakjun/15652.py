# N, M = map(int,input().split())
# INF = 0XFFFFFFFF
# p = [INF]*M
# def perm(idx):
#
#     if idx == M:
#         # 비감소인 경우 else 진행
#         for i in range(M-1):
#             if p[i] > p[i+1]:
#                 break
#
#         else:
#             for i in range(M):
#                 print(p[i], end=' ')
#             print()
#
#         return
#
#     if idx > 1:
#         if p[idx-1] > p[idx]:
#             return
#
#     # 다음 수 넣기
#     for i in range(1,N+1):
#         p[idx] = i
#         perm(idx+1)
#
# perm(0)





N, M = map(int,input().split())
INF = 0XFFFFFFFF
p = [INF]*M
def perm(idx, before):

    if idx == M:
        print( ' '.join(map(str,p)))

        return


    # 다음 수 넣기
    # 비감소해야하므로, before부터 커지는 순서대로 넣음
    for i in range(before,N+1):
        p[idx] = i
        perm(idx+1, i)

perm(0,1)