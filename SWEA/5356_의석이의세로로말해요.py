import sys
sys.stdin = open("5356_input.txt")


T = int(input())
for tc in range(1,T+1):
    # 5줄씩 읽기
    arr = [list(input()) for _ in range(5)]
    result = ''
    # 열 : 0~14
    for c in range(15):
    # 행 : 0~4
        for r in range(5):
            # try except
            try: # 결과에 계속 더하기
                result += arr[r][c]

            except IndexError:
                pass
    print(f'#{tc} {result}')
