N, M = map(int,input().split())

#
# def perm(idx, selected):  # idx가 현재 p의 몇번째에 넣을 것인지에 대한 idx,
#     # selected 는 선택한 갯수
#     if selected == M:
#         for i in range(M):
#             print(p[i], end= ' ')
#
#         print()
#
#
#     else:
#         for i in range(N):
#             if used[i] == 0:
#                 used[i] = 1
#                 p[idx] = i+1
#                 perm(idx+1, selected+1)
#                 used[i] = 0

def perm2(idx):  # idx가 현재 p의 몇번째에 넣을 것인지에 대한 idx 및 선택한 갯수
    if idx == M:
        for i in range(M):
            print(p[i], end= ' ')

        print()


    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                p[idx] = i+1
                perm2(idx+1)
                used[i] = 0

p = [0]*N
used = [0]*N

perm2(0)