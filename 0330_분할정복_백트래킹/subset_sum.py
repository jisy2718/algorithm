# 부분집합의 합이 10인 경우 출력

N = 10
arr = list(range(1,N+1))
selected = [0]*(N)
cnt = 0
# 각 index 요소가 부분집합
def powerset(selected, idx, sum_value): # sum_value는 백트래킹 위한 것
    global cnt
    if sum_value > 10:
        return

    if idx == N:
        sum_cur = 0
        sub_set = []
        for i in range(len(selected)):
            if selected[i] == 1:
                sum_cur += arr[i]
                sub_set.append(arr[i])
                cnt += 1

        if sum_cur == 10:
            print(sub_set)
                # print(arr[i], end=' ')
        # print()
        # print(selected)
        return

    selected[idx] = 1
    powerset(selected,idx+1,sum_value+ arr[idx])
    selected[idx] = 0
    powerset(selected,idx+1,sum_value)

powerset(selected,0,0)
print(cnt)



# selected 없이 구현
def powerset2(idx, sum_value,sub_set):
    if sum_value > 10:
        return

    if idx == N :
        print(sub_set)
        # if sum_value==10:
        #     print(sub_set)
        return
    sub_set.append(arr[idx])
    powerset2(idx+1, sum_value+arr[idx], sub_set)
    sub_set.pop()
    powerset2(idx +1, sum_value , sub_set)

powerset2(0,0,[])