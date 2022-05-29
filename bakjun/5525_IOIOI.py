N = int(input())
M = int(input())
S = input()

# IOIOIOIOI... 꼴로 이어지는 것 개수 세기
# IOI : 4
# IOIOI : 3개
# IOIOIOI : 2개
# 각 IOIOIOIOI... 길이 알면 IOIOIOI.. 가 그 안에 몇개인지 알 수 있음


cnt = 1
result = []
flag = False
for k in range(M):
    # 개수 세는 경우
    if flag == True:
        if k != 0:
            if S[k - 1] == 'I' and S[k] == 'O':
                cnt += 1
                # 마지막 까지 경우 센 경우
                if k == M-1:
                    result.append(cnt-1)
            elif S[k - 1] == 'O' and S[k] == 'I':
                cnt += 1
                if k == M-1:
                    result.append(cnt)
            # 중간에 실패하는 경우
            elif S[k - 1] == S[k]:
                if S[k] == 'I':  # IOIOII 꼴
                    result.append(cnt)
                    flag == True
                    cnt = 1
                else:  # IOIOIOO 꼴
                    result.append(cnt - 1)
                    flag = False
                    cnt = 0



    # 개수 세지 않는 경우 -> 개수 세기 시작
    elif flag == False:
        if S[k] == 'I':
            flag = True
            cnt = 1

target = 2*N + 1
count = 0

for num in result:
    if num >= target:  # 9  / 3,   IOIOIOIOI
        count += (num-target)//2 + 1
print(count)

