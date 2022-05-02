def same(N,lst):
    if N == 1:
        return True

    start = lst[0][0]
    for i in range(N):
        for j in range(N):
            if start != lst[i][j]:
                return False
    return True


def dfs(N, lst, loc):  #loc 1,2,3,4 : 좌상, 우상, 좌하, 우하
    global result

    if same(N,lst):
        num = str(lst[0][0])
        #
        # if loc == 1:
        #     num = '(' + num
        # elif loc == 4:
        #     num = num + ')'

        result =  result + num
        # print(result)

    else:

        leftupper = [ row[:N//2] for row in lst[:N//2]  ]
        rightupper = [ row[N//2:] for row in lst[:N//2] ]
        leftlower = [ row[:N//2] for row in lst[N//2:]  ]
        rightlower = [ row[N//2:] for row in lst[N//2:] ]
        boxes = [leftupper,rightupper,leftlower,rightlower]
        for i in range(len(boxes)):
            box = boxes[i]
            if not same(N//2, box):
                result = result + '('
                dfs(N//2, box, i+1)
                result = result + ')'
            else:
                dfs(N//2,box,i+1)
        #
        # dfs(N // 2, leftupper, 1)
        # dfs(N // 2, rightupper, 2)
        # dfs(N // 2, leftlower, 3)
        # dfs(N // 2, rightlower, 4)
        #




n = int(input())
arr = [list(map(int,input())) for _ in range(n)]
result = ''
loc = 0

# if same(n,arr):
#     q = 1
#     while n > 1:
#         n //= 2
#         q +=1
#     result = arr[0][0]
#     result = '('*q + result + ')'*q

dfs(n,arr,loc)

if not same(n,arr):
    result = '(' + result + ')'
# if n != 1:
#     result = '(' + result + ')'
print(result)




#------------------------------------------------sol2------------------------------------------
# def same(N,lst):
#     if N == 1:
#         return True
#
#     start = lst[0][0]
#     for i in range(N):
#         for j in range(N):
#             if start != lst[i][j]:
#                 return False
#     return True
#
#
# def dfs(N, lst, loc ,step):  #loc 1,2,3,4 : 좌상, 우상, 좌하, 우하
#     global result
#
#     if same(N,lst):
#         num = str(lst[0][0])
#         left = '('
#         right = ')'
#         if step >= 4:
#             left = left*(step-3)
#             right = right*(step-3)
#
#         if loc == 1:
#             num = left + num
#         elif loc == 4:
#             num = num + right
#
#         result = result + num
#
#     else:
#         leftupper = [ row[:N//2] for row in lst[:N//2]  ]
#         rightupper = [ row[N//2:] for row in lst[:N//2] ]
#         leftlower = [ row[:N//2] for row in lst[N//2:]  ]
#         rightlower = [ row[N//2:] for row in lst[N//2:] ]
#
#
#         dfs(N // 2, leftupper, 1,step+1)
#         dfs(N // 2, rightupper, 2,step+1)
#         dfs(N // 2, leftlower, 3,step+1)
#         dfs(N // 2, rightlower, 4,step+1)
#
#
#
#
#
# n = int(input())
# arr = [list(map(int,input())) for _ in range(n)]
# result = ''
# loc = 0
#
# dfs(n,arr,loc,1)
#
# result = '(' + result + ')'
# print(result)
#----------------------------------------------------------------------------------

#
# 8
# 11111111
# 11110000
# 11110101
# 11110000
# 11111111
# 11111111
# 11111111
# 11110101