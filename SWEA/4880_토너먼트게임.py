def match(p1, p2):  # p1 = (idx, 가위바위보) 꼴
    loss = {1: 2, 2: 3, 3: 1}  # 가위:바위, 바위:보, 보:가위  로 예를들면 가위는 dict[가위] 에게 진다.

    # 1. 비기기
    if p1[1] == p2[1]:
        return p1
    # 2. p1이 지기
    elif loss[p1[1]] == p2[1]:
        return p2

    # 3. p1이 이기기
    else:
        return p1


def divide_match(idx_value_lst: list, start: int, end: int):
    result = []
    mid = (start + end) // 2
    left = idx_value_lst[start:mid + 1]
    right = idx_value_lst[mid + 1: end + 1]

    # 승부를 겨룰 수 있는 경우
    # 1) 둘 다 원소가 1개
    if len(left) == 1 and len(right) == 1:
        result.append(match(left[0], right[0]))
        return result
    # 2) left 가 원소 1개이고 right는 없는 경우
    elif len(left) == 1 and not right:
        result.append(left[0])
        return result
    else:
        result.extend(divide_match(idx_value_lst, start, mid))
        result.extend(divide_match(idx_value_lst, mid + 1, end))

    return result


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    idx_value_lst = [[i, lst[i]] for i in range(N)]

    result = divide_match(idx_value_lst, 0, len(idx_value_lst) - 1)
    while len(result) > 1:
        result = divide_match(result, 0, len(result) - 1)

    # 사람의 번호는 idx + 1 이다.
    print(f'#{tc} {result[0][0]+1}')
