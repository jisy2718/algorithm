# input = "921 + 356"
lst = ['921','+','356'] # lst = input().split()

# 원래 결과
# a + b  = c
a = int(lst[0])
b = int(lst[2])
c = a + b

# 바꾼 결과
a_string = str(a)
a_r = int(a_string[::-1])

b_string = str(b)
b_r = int(b_string[::-1])

c_string = str(c)
c_r = int(c_string[::-1])

print(a_r, b_r, c_r)



# 최대한 짧은 이동거리 찾기
length = len(a_string)  # length == 3
INF = 0Xfffffffffffffff
visited = [0]*((10**length)*2-1) # index : 0~ 1998  : 1 ~ 999 / -1 ~ -999(==1000)  /0 은 안씀

visited = [INF]*(10**length)   # index : 0 ~ 999 if length == 3

target = c_r % (10*length)




# bfs
q = []
cnt = 0
q.append([cnt, a_r, b_r])
visited[a_r+b_r] = 0
limit = 100
while q:
    # print(q)
    c_cnt , c_a_r, c_b_r = q.pop(0)
    # 1. 종료 조건
    if c_a_r + c_b_r == target:
        c_cnt = limit+1


    # 2. 할 수 있는 것 1개 씩 하기
    # 2-1. a바꾸기
    if c_cnt <= limit:
        for i in range(length):
            a_r_string = str(c_a_r)
            if a_r_string[i] != '9':  # i==0 : 맨 앞자리 수
                new_a_r = c_a_r + 10 ** (length - i - 1)

                # 계산한 결과가 이전보다 좋다면 BFS 진행
                cur_num = (new_a_r + c_b_r) % 1000
                if visited[cur_num] > c_cnt + 1:
                    visited[cur_num] = c_cnt + 1
                    q.append([c_cnt + 1, new_a_r, c_b_r])

            if a_r_string[i] != '0':
                if i != 0:
                    new_a_r = c_a_r - 10 ** (length - i - 1)

                else:
                    if a_r_string[0] != '1':
                        new_a_r = c_a_r - 10 ** (length - i - 1)

                # 계산한 결과가 이전보다 좋다면 BFS 진행
                cur_num = (new_a_r + c_b_r) % 1000
                if visited[cur_num] > c_cnt + 1:
                    visited[cur_num] = c_cnt + 1
                    q.append([c_cnt + 1, new_a_r, c_b_r])

        # 2-2. b바꾸기
        for i in range(length):
            b_r_string = str(c_b_r)
            if b_r_string[i] != '9':  # i==0 : 맨 앞자리 수
                new_b_r = b_r + 10 ** (length - i - 1)

                # 계산한 결과가 이전보다 좋다면 BFS 진행
                cur_num = (c_a_r + new_b_r) % 1000
                if visited[cur_num] > c_cnt + 1:
                    visited[cur_num] = c_cnt + 1
                    q.append([c_cnt + 1, new_a_r, c_b_r])

            if b_r_string[i] != '0':
                if i != 0:
                    new_b_r = c_b_r - 10 ** (length - i - 1)

                else:
                    if b_r_string[0] != '1':
                        new_b_r = c_b_r - 10 ** (length - i - 1)

                # 계산한 결과가 이전보다 좋다면 BFS 진행
                cur_num = (c_a_r + new_b_r) % 1000
                if visited[cur_num] > c_cnt + 1:
                    visited[cur_num] = c_cnt + 1
                    q.append([c_cnt + 1, c_a_r, new_b_r])

# print(visited[target-10:target+10])
print(visited[target])


# bfs
def bfs(cnt, a_r, b_r): # 현재 a_r - b_r = 값 경우 움직인 횟수는 cnt 개
    # 1. 종료조건
    if a_r + b_r == target:
        return visited[a_r+b_r] # or cnt

    # 최대값 넘어가면 종료
    if cnt > 30:
        return



    else:

        # 2. 할 수 있는 것 1개 씩 하기
        # 2-1. a바꾸기

        for i in range(length):
            a_r_string = str(a_r)
            if a_r_string[i] != '9':   # i==0 : 맨 앞자리 수
                new_a_r = a_r + 10**(length-i-1)


                # 계산한 결과가 이전보다 좋다면 BFS 진행
                cur_num = (new_a_r + b_r)%1000
                if visited[cur_num] > cnt+1:
                    visited[cur_num] = cnt+1
                    bfs(cnt+1, new_a_r, b_r)

            if a_r_string[i] != '0':
                if i != 0:
                    new_a_r = a_r - 10 **(length-i-1)

                else:
                    if a_r_string[0] != '1':
                        new_a_r = a_r - 10 **(length-i-1)

                # 계산한 결과가 이전보다 좋다면 BFS 진행
                cur_num = (new_a_r + b_r)%1000
                if visited[cur_num] > cnt+1:
                    visited[cur_num] = cnt+1
                    bfs(cnt+1, new_a_r, b_r)






