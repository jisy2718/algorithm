import sys
sys.stdin = open('input3.txt')


T = int(input())
for tc in range(1,T+1):
    F, N = map(int,input().split())
    arr = list(map(int,input().split()))


    def get_hand_dic(lst):
        hand_dic = {}
        for num in lst:
            if num in hand_dic:
                hand_dic[num] += 1
            else:
                hand_dic[num] = 1
        return hand_dic

    def get_luck(hand_dic):
        max_hands = hand_dic[arr[0]]
        max_al = arr[0]
        for num in arr:
            if hand_dic[num] > max_hands:
                max_al = num

        return max_al

    def check(lst):
        s = lst[0]
        for i in range(1,len(lst)):
            if lst[i] != s:
                return -1

        else:
            return 1



    while F>0:
        turn = len(arr)
        hand_dic = get_hand_dic(arr)
        luck_al = get_luck(hand_dic)  # 손을 다시 넣지 않을 외계인
        flag = False                  # 손을 다시 넣지 않는 동작을 했는지 안했는지    m
        while turn >0 and F>0:
            if check(arr) == 1:
                result = arr[0]
                F = 0
                break

            F -= 1
            # if tc == 2:
            #     print(arr)
            cur = arr.pop(0)
            if cur == luck_al and flag==False:
                flag = True


            elif cur != luck_al or flag == True:
                arr.append(cur)
            # print(arr)

            turn -= 1
            if F == 0:
                result = cur



    print(f'#{tc} {result}')





