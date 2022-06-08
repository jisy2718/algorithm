import sys
sys.stdin = open('algo_input.txt')

# 1. input 받기
# a + b = c
nums = list(map(int,input().split()))
a,b,c = nums

# 2. 숫자 뒤집기
rnums = []
for num in nums:
    rnum = int(str(num)[::-1])
    rnums.append(rnum)

print('input is : ', nums)
print('reversed input is : ', rnums)



# 3. 범위확인하기
ra , rb , rc = rnums # 852 , 853, 616

# (3,3) 자리 이용 경우
min1 = (ra//100)*100 + (rb//100)*100 # 800 + 800
max1 = min1 + 99 + 99                # 899 + 899

# (3,2) 자리 이용 경우
min2 = (ra//100)*100 + (rb//100)*10  # 800 + 80
max2 = min2 + 99 + 9                 # 899 + 89

# (3,1) 자리 이용 경우
min3 = (ra//100)*100 + rb//100
max3 = min3 + 99

# (2,3) 자리 이용 경우

# (2,2) 자리 이용 경우

# (2,1) 자리 이용 경우

# (1,3) 자리 이용 경우

# (1,2) 자리 이용 경우


# (1,1) 자리 이용 경우
min9 = (ra//100) + (rb//100)
max9 = min9


h1 = ra//100
h2 = rb//100
for used1 in range(3):
    for used2 in range(3):
        cur_min = h1*10**used1 + h2*10**used2  # 800 + 800 / 8*100 + 8*100
        cur_max = cur_min + (10**used1 - 1) + (10**used2 -1)
        if cur_min <= rc <= cur_max:
            print(f'True {cur_min} <= {cur_max}')
        else:
            print('False')




def bfs(nums):
    target = nums[-1]
    nums = nums[:-1].copy()
    h1 = nums[0]//100
    h2 = nums[1]//100

    INF = 0xfffffffffffffff
    visited = [INF]*1000
    q = [[0, nums]]
    visited[sum(nums)] = 0

    while q:
        cmove, cnums = q.pop(0)

        if sum(cnums) == target:
            visited[target] = cmove
            return cmove

        else:
            # 요기 조작해줘야함
            for used1 in range(3):
                for used2 in range(3):
                    num1 = cnums[0]//(10**(2-used1))
                    num2 = cnums[1]//(10**(2-used2))

                    if  num1+num2 <=999:
                        # bfs진행
                        if visited[num1 + num2] <= cmove:
                            q.append([cmove+1, [num1,num2]])





