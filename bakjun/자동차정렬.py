import heapq

data = list('CAABBAABBC')
# data = list('ABCDDAD')
# data = list('ABCDDADA')
# data = list('BAAAAAAAD')
# data = list('AAAABBCBBC')
N = len(data)
print(''.join(data))



def check_done(data):
    data_dict = dict()
    i = 0
    while i < len(data):
        num = data[i]
        # print(num, data_dict)
        # num이 처음 나온 문자라면 data_dict에 추가하고, 이어지는 것 개수세기
        if not data_dict.get(data[i]):
            data_dict[data[i]] = 1
            while i < len(data) and data[i] == num:
                i += 1
            continue
        # num이 처음 나온 문자가 아니라면, 아직 정렬되지 않았음.
        else:
            return False
        # if not에서 이어진 같은 문자 개수 모두 세었으면, 다음 문자로 넘어가기
        i += 1
    return True

from collections import deque
def solve(data):
    queue = deque([])  # 교환 대상 배열 저장, 교환하고 나서 비용 저장하기

    visited_dp = {}
    str_data = ''.join(data)
    before = []
    queue.append([0,str_data,before])
    # heapq.heappush(queue,(0,str_data)) # ( 비용, 현재문자열 )
    visited_dp[str_data] = 0
    results = []
    while queue:
        cur_cost, head , before = queue.popleft()
        # cur_cost, head = heapq.heappop(queue)
        # 완성 되었으면 저장
        if check_done(head):
            results.append([cur_cost,head, before])
        if head == 'AAABBCBBC':
            print("find_target", cur_cost, head, before)

        before = [cur_cost, head] + before
        tmp_list = list(head)
        for i in range(N):
            for j in range(i+1,N):
                tmp_list[i],tmp_list[j] = tmp_list[j],tmp_list[i]
                str_tmp_list = ''.join(tmp_list)
                new_cost = cur_cost + abs(j-i) # 교환 비용

                if str_tmp_list not in visited_dp:
                    visited_dp[str_tmp_list] = new_cost # 현재가지 비용 넣어주기
                    queue.append([new_cost, str_tmp_list, before] )
                elif str_tmp_list in visited_dp:
                    if visited_dp[str_tmp_list] > new_cost:
                        visited_dp[str_tmp_list] = new_cost
                # 교환 해준 것 원래대로 되돌리고, 다음 교환 진행하기
                tmp_list[i], tmp_list[j] = tmp_list[j], tmp_list[i]
    if not results:
        return -1
    else:
        results.sort()
        return results


results = solve(data)
for result in results:
    print(result)