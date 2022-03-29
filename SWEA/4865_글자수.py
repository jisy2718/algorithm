
T = int(input())
for tc in range(1, T + 1):
    str1_set = set(input())
    str2 = input()

    max_count = 0
    for char in str1_set:  # 비교할 문자
        cur_count = 0  # 해당문자 count 초기화
        for char_in_str2 in str2:  # 전체 텍스트의 문자와 비교
            if char_in_str2 == char:
                cur_count += 1  # 일치하면 count 해주기
        if max_count < cur_count:  # max 찾는 것이므로 비교 후 업데이트
            max_count = cur_count
    print(f"#{tc} {max_count}")