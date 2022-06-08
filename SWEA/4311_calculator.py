# 1. bfs 실패
# T = int(input())
# for tc in range(T):
#     N, O, M = map(int,input().split())  # 이용가능 숫자개수, 이용가능 연산자 개수, 최대 터치 가능한 횟수
#     nums = list(map(int,input().split()))
#     cal = list(map(int,input().split())) # 1 : +, 2:- , 3:*, 4://
#     goal = int(input())
#
#     INF = 0xffffffffffffff
#     visited=[INF]*1000
#     q = []
#     for num in nums:
#         visited[num] = 1
#         q.append([num,1,True])
#     flag = False
#     while q:
#         cur_num, cur_touch, done = q.pop(0)
#
#         if cur_num == goal:
#             if done == False:
#                 print(cur_touch+1) # = touch
#             else:
#                 print(cur_touch)
#             flag = True
#             break
#
#         # 1. 연산을 할 수 있고
#         for i in range(O):
#             for num in nums:
#                 if cal[i] == 1:
#                     next_num = cur_num + num
#
#                 elif cal[i] == 2:
#                     next_num = cur_num - num
#
#                 elif cal[i] == 3:
#                     next_num = cur_num * num
#                 else:
#                     next_num = cur_num//num if num != 0 else None
#
#                 if next_num != None and 0 <= next_num and next_num<1000 and visited[next_num] > cur_touch+2:
#                     q.append([next_num, cur_touch+2, False])
#                     visited[next_num] = cur_touch+2
#
#
#
#         # 2. 숫자를 더 누를 수도 있다
#         for num in nums:
#             next_num = cur_num*10 + next_num
#             if 0 <= next_num and next_num < 1000 and visited[next_num] > cur_touch+1:
#                 q.append([next_num, cur_touch + 1, True])
#                 visited[next_num] = cur_touch+1
#
#     if flag == False:
#         print(-1)


# 2. bfs2
T = int(input())
for tc in range(T):
    N, O, M = map(int,input().split())  # 이용가능 숫자개수, 이용가능 연산자 개수, 최대 터치 가능한 횟수
    nums = list(map(int,input().split()))
    cals = list(map(int,input().split())) # 1 : +, 2:- , 3:*, 4://
    cals_dic = {}
    cals_dic={1:'+', 2:'-', 3:'*', 4:'/'}
    goal = int(input())


    comb_nums = []
    for num1 in nums:
        for num2 in nums:
            for num3 in nums:
                new_num = num1*100 + num2*10 + num3
                if new_num <1000:
                    comb_nums.append(str(new_num))

    comb_cals_nums = []
    for cal in cals:
        for num in comb_nums: #
            cal_num = cals_dic[cal] + num  # str 형태임.
            comb_cals_nums.append([cal_num, len(cal_num)])



    INF = 0xffffffffffffff
    visited=[INF]*1000
    q = []
    for num in nums:
        visited[num] = 0
        q.append([str(num),0, True])
    flag = False
    while q:
        cur_num, cur_touch , done= q.pop(0)
        cur_num = int(cur_num)

        for cal_num_touch in comb_cals_nums:
            cal_num , touch = cal_num_touch

            if cal_num[0] == '+':
                next_num = cur_num + int(cal_num[1:])

            elif cal_num[0] == '-':
                next_num = cur_num - int(cal_num[1:])

            elif cal_num[0] == '*':
                next_num = cur_num * int(cal_num[1:])

            elif cal_num[0] == '/':
                if int(cal_num[1:])!=0:
                    next_num = cur_num // int(cal_num[1:])
                    next_num = int(next_num)
                else:
                    next_num = None

            if next_num != None and done==True and 0 < next_num and next_num <1000 and visited[next_num] > cur_touch + touch+1:
                # 99 +111 꼴이 진행된 건데, 99를 현재 touch = 1로 세고 있으므로 1 추가해줘야 함
                q.append([str(next_num), cur_touch+touch+1,False])
                visited[next_num] = cur_touch + touch +1
            elif next_num != None  and done==False and 0 < next_num and next_num <1000 and visited[next_num] > cur_touch + touch:
                q.append([str(next_num), cur_touch + touch,False])
                visited[next_num] = cur_touch + touch

        if done == True:
            for num in nums:
                next_num = int(str(cur_num) + str(num))
                if 0 < next_num and next_num < 1000 and visited[next_num] > cur_touch + 1:
                    q.append([str(next_num), cur_touch+1,True])
                    visited[next_num] = cur_touch + 1






    if visited[goal] == INF:
        print(-1)
    else:
        print(visited[goal]+1)







# ------------------------------------------------------------------------------------------------------
# # 2. dfs
# T = int(input())
# for tc in range(T):
#     N, O, M = map(int,input().split())  # 이용가능 숫자개수, 이용가능 연산자 개수, 최대 터치 가능한 횟수
#     nums = list(map(int,input().split()))
#     cal = list(map(int,input().split())) # 1 : +, 2:- , 3:*, 4://
#     goal = int(input())
#     nums.append(0)
#
#     comb_nums = []
#     for num1 in nums:
#         for num2 in nums:
#             for num3 in nums:
#                 new_num = num1*100 + num2*10 + num3
#                 if new_num <1000:
#                     comb_nums.append(new_num)
#
#
