from collections import deque

T = int(input())
# front가 어딘지 파악해서, pop으로 lst 변경시키기. 
# 그리고 마지막에 lst를 front == 0 이라면 그대로, front == -1 이라면 뒤로 뒤집어서 프린트
for _ in range(T):
    order = input()
    n = int(input())
    lst = input()
    if lst != '[]':
        lst = deque(map(int, lst.strip('[').strip(']').split(',')))
    else:
        lst = []


    flag = True  # error 경우, False로 바뀜
    front = 0
    for i in range(len(order)):

        cur = order[i]
        if cur == 'R':
            if front == 0:
                front = -1

            else:
                front = 0

        else:  # cur == 'D' 삭제
            if n == 0:
                flag = False
                print('error')
                break
            else:
                n -= 1
                if front == 0:
                    lst.popleft()
                else:
                    lst.pop()

                # print(f'현재 lst {lst} cur front is {front}')

    lst = list(lst)
    if front == 0 and flag == True:
        print(lst)
    elif front == -1 and flag == True:
        print(lst[::-1])

