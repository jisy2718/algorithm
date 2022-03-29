

import sys
sys.stdin = open("10726_input.txt")

def decimal_to_binary(M:int)->str:
    result = ''
    while M:
        res = M % 2
        result = str(res) + result
        M //= 2
    return result

T = int(input())
for tc in range(1,T+1):
    result = "OFF"
    N, M = map(int,input().split()) # 마지막 N 비트 / 정수 M
    if M < 2**(N-1):
        print(f'#{tc} {result}')
    else:
        binary_M = decimal_to_binary(M)
        if binary_M[-N:] == '1'*N:
            result = 'ON'

        print(f'#{tc} {result}')
        # print(binary_M)


