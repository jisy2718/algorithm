# 더하는 수가 1 ~ 4자리 수이고, 결과는 1~ 5자리 수인 경우

import sys
sys.stdin = open('algo_input.txt')
for tc in range(1,51):
    # 1. input 받기
    # a1 + a2 + ... an = c
    tc_dummy = input()
    arr = input()
    arr = arr.split('=')
    c = str(int(arr[1]))

    nums = arr[0]
    nums = nums.split('+')
    nums = nums + [c]

    nums = list(map(int,nums))  # 정수화 [a1,a2,...,an,c]

    # 2. 숫자 뒤집기
    rnums = []
    for num in nums:
        rnum = int(str(num)[::-1])
        rnums.append(rnum)
    goal = rnums[-1]
    # print('input is : ', nums)
    # print('reversed input is : ', rnums)


    # 3. 답 구하기
    n = len(nums) - 1
    # input으로 받은 i 번째 숫자를 몇 번째 자리까지 이용할지를 used 를 이용해서 표기
    used = [0]*n   # used[4] == 2 라면, 5번째 숫자는 10**2 단위까지 (xxx 꼴) 이용한다는 의미.
    result = 0
    def find_min_max(idx):
        global result
        # [1] 결과 부분
        if idx == n:
            cur_min = 0
            cur_max = 0
            # print(used)
            for i in range(n):
                num = rnums[i]
                ilen = len(str(num))      # num의 자리수
                ih = num//(10**(ilen-1))  # num의 첫 글자

                # 최소값과 최대값 범위
                # used[i]= 2라면 이 경우 (ih)xx 꼴 숫자(ih는 num의 첫숫자)
                cur_min += ih*(10**used[i])                      # (ih)xx의 최소값은 (ih)00 이고
                cur_max += ih*(10**used[i]) + (10**used[i]-1)    # (ih)xx의 최대값은 (ih)99 이다.


            if cur_min <= goal <= cur_max:
                result = 1    # goal을 달성할 수 있으면 result = 1로 변환
            else:
                return

        # [2] 재귀호출 부분 ------------------------------------------------------------
        else:
            for i in range(5): # 5자리수까지 이용 1 ~ 9999 , xxxxx
                used[idx] = i # i==4 => 10**4 == xxxxx
                find_min_max(idx+1)
    #------------------------------------------------------함수 끝---------------------

    find_min_max(0)
    print(f'#{tc} {result}')
