# 자연수에 대해서, 리스트를 이용한 counting sort
def counting_sort2(l: list, k: int):
    # 1. 기본 세팅
    count = [0] * k  # count 하는 list 는 1~k 까지의 값이 몇 번 input list에서 나타나는지 count한 것
    l_len = len(l);
    result = [0] * l_len  # 결과 list

    # 2. counting
    # 2-1. counting
    for num in l:
        count[num - 1] += 1  # 숫자 num을 count의 num-1 번째 index에 넣어줌

    # 2-2. cumulative counting
    for j in range(1, k):
        count[j] += count[j - 1]

    # print(count)

    # 3. making result list
    for num in l:
        # print(num)
        result_index = count[num - 1] - 1
        result[result_index] = num
        count[num - 1] -= 1
    return result