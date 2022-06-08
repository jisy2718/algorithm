# 더하는 수와 결과가 모두 3자리만 가능한 경우 풀이.

import sys
sys.stdin = open('algo_input.txt')
for tc in range(1,51):
    # 1. input 받기
    # a1 + a2 + ... an = c
    nums = list(map(int,input().split()))

    # 2. 숫자 뒤집기
    rnums = []
    for num in nums:
        rnum = int(str(num)[::-1])
        rnums.append(rnum)
    goal = rnums[-1]
    # print('input is : ', nums)
    # print('reversed input is : ', rnums)

    n = len(nums) - 1
    used = [0]*n   # input으로 받은 i 번째 숫자를 몇 번째 자리까지 이용할지 : used[4] == 2 라면, 5번째 숫자는 10*2 단위까지 (xxx 꼴) 이용한다는 의미.
    result = 0
    def find_min_max(idx):
        global result
        # 1. 결과 부분
        if idx == n:
            cur_min = 0
            cur_max = 0
            for i in range(n):
                num = rnums[i]
                # rnums[i]의 자리수
                ilen = len(str(num))      # num의 자리수
                ih = num//(10**(ilen-1))  # num의 첫 글자

                # ilen ==4 라면, used[i]는 3까지 가능 : 예를들어 i번째 수가 1329라면 1xxx , 1xx, 1x, 1 총 4가지 경우로 활용 가능함.
                if used[i] < ilen: # 즉, 자리수가 유효한 경우에만 : ilen == 2(10~99) 인데 used[i] == 2(10**2) or 3(10**3)일 수 없음
                    cur_min += ih*(10**used[i])
                    cur_max += ih*(10**used[i]) + (10**used[i]-1)

                # 유효하지 않은 경우는 그냥 함수 끝내기
                else:
                    return

            if cur_min <= goal <= cur_max:
                result = 1    # goal을 달성할 수 있으면 result 변환
            else:
                return

        # 2, 재귀호출 부분 ------------------------------------------------------------
        else:
            for i in range(4):
                used[idx] = i
                find_min_max(idx+1)
    #------------------------------------------------------함수 끝---------------------

    find_min_max(0)
    print(f'#{tc} {result}')



