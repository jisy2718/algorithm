from collections import deque



T = int(input())
for tc in range(1,T+1):
    s, e = map(int,input().split())

    max_num = 1000000*2

    visited = [0]*max_num

    min_cal = 10000000
    queue = deque([[s,0]])
    while queue:
        cur_loc, cur_cal = queue.popleft()

        if cur_loc == e:
            min_cal = cur_cal
            break

        elif cur_loc > e:
            candi = [cur_loc-1,cur_loc-10]

        else:
            candi = [cur_loc*2, cur_loc-10, cur_loc-1, cur_loc+1]

        for new_loc in candi:
            if visited[new_loc] == 0 and 1 <= new_loc <=max_num:
                queue.append([new_loc,cur_cal+1])
                visited[new_loc] = 1


    print(f"#{tc} {min_cal}")