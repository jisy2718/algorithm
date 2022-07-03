

string = input().strip()
bomb = input().strip()

# 폭탄의 길이
bomb_len = len(bomb)

# 스택을 이용해서 해결!
stack = []

# stack에 폭탄의 몇번째 글자(i)인지와 글자가 무엇인지 저장
i = 0
for char in string:
    if char == bomb[i]:
        stack.append([i,char])
        i += 1
    elif char == bomb[0]:
        stack.append([0,char])
        i = 1

    else:
        stack.append([-1, char])
        i = 0   # bomb의 시작일 경우만 앞으로 들어올 수 있음

    # i 가 폭탄 길이만큼 세어지면, 폭탄 만든 것임.
    # bomb을 만든 경우
    if i == bomb_len:
        # for _ in range(bomb_len):
        #     stack.pop()   # pop 해주기
        del stack[-i:]
        if stack:
            i = stack[-1][0] +1  # 이전 폭탄문자열에서 다시시작!
        else:
            i = 0  # 초기화해주기.



# 뺄 수 있는 만큼 다 빼기
while i == bomb_len:
    for _ in range(bomb_len):
        stack.pop()
    if stack:
        i = stack[-1][0] +1 # 이전 폭탄문자열에서 다시시작!
    else:
        i = 0  # 초기화해주기.


if not stack:
    print('FRULA')
else:
    answer = ''
    for char in stack:
        answer += char[1]
    print(answer)
    # for char in stack:
    #     print(char[1],end='')
