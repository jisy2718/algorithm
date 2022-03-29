import sys
sys.stdin = open('hw_1240_input.txt')

# 1. 데이터 읽기 /  10진수로 8글자임.
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [input() for _ in range(N)] # ['00000','00000','00000']꼴

    code = ''
    flag = False
    for r in range(N):
        for c in range(M-1,-1,-1):
            if arr[r][c] == '1':
                code = arr[r][c-55:c+1]
                flag = True
                break
        if flag == True:
            break





    # 2. 10진법으로 바꾸기
    binary_to_decimal = {'0001101':0, '0011001':1, '0010011':2,
                     '0111101':3, '0100011':4, '0110001':5,
                     '0101111':6, '0111011':7, '0110111':8, '0001011':9}
    result = [0]*9
    for i in range(0,8):
        cur = code[7*i: 7*i+7]
        result[i+1] = binary_to_decimal.get(cur)

    # 3. 검증하기 & 결과
    # 1,3,5,7 index의 값이 홀수번째 값 / 2,4,6 번째
    if ( (result[1] + result[3] + result[5] + result[7])*3 + result[2] + result[4] + result[6] + result[8] )%10 ==0:
        print(f'#{tc} {sum(result)}')
    else:
        print(f'#{tc} 0')


