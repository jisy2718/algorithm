T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))  # N : matrix 크기 / M : 회문의 길이
    arr = [list(input()) for _ in range(N)]
    arr_t = list(map(list, zip(*arr)))

    for target_arr in [arr, arr_t]:
        # 한줄씩 가면서 M//2 개 원소 저장한후 그 뒤의 M//2 개 원소와 비교
        for k in range(N):
            row = target_arr[k]
            palindrome = ''
            is_pal = list()  # M//2 개 이동하면서 순서대로 저장
            # N - M 번까지만 시작하면 됨. N -M , N-(M -1) , ... , N-1 : M 개
            for i in range(N - M + 1):

                for j in range(M // 2):
                    is_pal.append(row[i + j])

                # 그 뒤의 M //2 개와 비교
                # case 1 ) M is even num
                if not M % 2:
                    for j in range(M // 2):
                        if is_pal[M // 2 - 1 - j] == row[
                            i + j + M // 2]:  # is_pal 은 뒤에서부터 앞으로, row는 is_pal 이 끝난 위치부터 뒤로 가며 비교

                            is_pal.append(row[i + j + M // 2])  # 일치한다면 is_pal 뒤에 넣어주기

                            continue
                        else:
                            is_pal = []  # 초기화 후 다음 i에 대해 진행
                            break

                # case 2) M is odd num
                else:
                    is_pal.append(row[i + M // 2])  # 중간글짜 넣어주기
                    for j in range(M // 2):
                        if is_pal[M // 2 - j - 1] == row[
                            i + j + M // 2 + 1]:  # is_pal 은 뒤에서부터 앞으로, row는 is_pal 이 끝난 위치부터 뒤로 가며 비교

                            is_pal.append(row[i + j + M // 2 + 1])  # 일치한다면 is_pal 뒤에 넣어주기

                            continue
                        else:
                            is_pal = []  # 초기화 후 다음 i에 대해 진행
                            break

                # 회문을 찾은 경우
                if len(is_pal) == M:
                    break
            if len(is_pal) == M:
                for i in range(len(is_pal)):
                    palindrome = palindrome + is_pal[i]

            if palindrome:
                print(f"#{tc} {palindrome}")
                break