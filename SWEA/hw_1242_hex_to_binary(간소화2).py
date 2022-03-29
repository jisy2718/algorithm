# hex 자체를 binary로 바꿔서 해야겟음
# 간소화 1에 비해서, find_num() 함수를 없앴음.


import sys
sys.stdin = open('hw_1242_input.txt')

codes = {(2,1,1):0, (2,2,1):1, (1,2,2):2,
         (4,1,1):3, (1,3,2):4, (2,3,1):5,
         (1,1,4):6, (3,1,2):7, (2,1,3):8, (1,1,2):9}

hex_to_bin = {'0':'0000', '1':'0001', '2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}

#
# def hex_to_binary(h):
#     decimal_result = 0
#     if h in '0123456789':
#         decimal_result = ord(h) - ord('0')
#     else:
#         decimal_result = ord(h) - ord('A') + 10
#
#     binary_result = ''
#     for _ in range(4):
#         res = decimal_result % 2
#         binary_result = str(res) + binary_result
#         decimal_result //= 2
#
#     return binary_result

def delete_zero(crypto:str):
        if not crypto:
            return None
        i = len(crypto) - 1
        while i>=0:
            if crypto[i] == '0':
                i -= 1
            else:
                break
        return(crypto[:i+1])

# def find_num(cnts2,cnts3, cnts4):  # 이진수 뒷자리 1,0,1 개수 찾은 것으로 이를 이용해 10진수 수 찾음
#     Gcd = min(cnts2,cnts3,cnts4)
#     code = (int(cnts2/Gcd), int(cnts3/Gcd), int(cnts4/Gcd))
#     res = Gcd*(7 - cnts2/Gcd - cnts3/Gcd - cnts4/Gcd) # 해당 숫자 앞에 채워진 0
#     cur_num = codes.get(code)
#
#     return cur_num, res  # cur_num 은 10진수 수, res는 cur_num의 맨 앞 0의 개수

def discrimination(decimals):  # 찾은 암호문이 올바른지 판단
    odd = 0
    even = 0
    for i in range(1,8,2):
        odd += decimals[i]
        even += decimals[i+1]

    if (odd*3 + even) % 10 == 0:
        return (odd+even)
    else:
        return 0

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [input().strip() for _ in range(N)]

    arr = set(arr)

    # arr을 이진수로 바꾸기
    hex_to_binary_cryptos = set()
    for hex_crypto in arr:
        result = ''
        flag = False
        for char in hex_crypto:
            binary = hex_to_bin[char]
            result = result + binary
        if '1' in result:
            flag = True

        if flag == True:
            # print(arr[r])
            hex_to_binary_cryptos.add(result)
    # print(f"#{tc} {hex_to_binary_cryptos}")

    results = set()
    for crypto in hex_to_binary_cryptos: # 맨 뒤에 0 다 잘라주기
        # 1. 뒤에 0 다 잘라주기
        crypto = delete_zero(crypto)
        i = len(crypto)-1 # i로 현재 위치 가리킨다.

        while i >= 0: #crypto가 남아 있는 경우에만
            # 숫자 8개 하나 만들기
            decimals = [0]*9 # 1 ~ 8 index 이용
            loc = 8
            # 숫자가 채워질 때까지
            while loc > 0:

            # 2. 뒤에서부터 3번 바뀌는 동안 개수 세고, 거기서 최소값(gcd)으로 나눠주기 & 그 다음 수 세서 i 옮겨주기

                # 십진법 숫자 1개 찾기 시작 --------------------------------------------------
                # codes 에 보면, 항상 1이 있으므로, 아래 세 값중 최소값이 gcd임
                cnts = [0]*5 # 1 ~ 4 index 이용
                while i >= 0 and crypto[i] == '1':
                    cnts[4] += 1         # 4자리 코드 중 4번째 자리 코드
                    i -= 1
                gcd = cnts[4]
                while i >= 0 and crypto[i] == '0':
                    cnts[3] += 1         # 4 자리 코드 중 3 번째 자리 코드
                    i -= 1
                if gcd > cnts[3]:
                    gcd = cnts[3]
                while i >= 0 and crypto[i] == '1':
                    cnts[2] += 1         # 4 자리 코드 중 2번째 자리 코드
                    i -= 1
                if gcd > cnts[2]:
                    gcd = cnts[2]  # gcd 찾기

                code = (int(cnts[2]/gcd), int(cnts[3] / gcd), int(cnts[4] / gcd)) # 뒤의 3자리만 가지고 코드를 구성가능
                res = gcd * (7 - cnts[2] / gcd - cnts[3] / gcd - cnts[4] / gcd)  # 해당 숫자 앞에 채워진 0 개수
                cur_num = codes.get(code)

                # -------------------------------------------------------------- 숫자 1개 찾기 끝

                i -= int(res) # 4 자리 코드 중 첫번째 자리 코드의 0 개수만큼 i를 앞으로 이동
                decimals[loc] = cur_num
                loc -= 1


            results.add(tuple(decimals))
            # print(decimals)

            # binary 코드의 시작점에 다다르지 않았다면,, 남은 코드 부분 다시 순환시작
            if i != -1:
                crypto = delete_zero(crypto[:i+1])
                i = len(crypto) - 1


    result = 0
    for decimal in results:
        result += discrimination(decimal)
    print(f'#{tc} {result}')







