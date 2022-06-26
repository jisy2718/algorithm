# A, B, C = map(int,input().split())
#
# lst = []
# lst_set = set()
# multiple = A
# while A not in lst_set :
#     A %= C
#     lst.append(A)
#     lst_set.add(A)
#     A *= multiple
#     A %= C
#     # print(A, lst_set)
#     if len(lst_set)==B:
#         break
#
#
# # A 가 lst_set에 있는 경우
# if A in lst_set:
#     # 반복 횟수 찾기
#     s = 0
#     while lst[s] != A:
#         s += 1
#
#     repeat_len = len(lst_set) -1 - s +1 # ( 끝 idx - 시작 idx + 1)
#     # 0, ..., s, ..., s+repeat_len-1, 다시 s index 부터 반복
#     # print(s, repeat_len)
#
#     r = (B-s) % repeat_len  # 총 B번 곱해야하는데, s+1 번 곱한 경우에 반복이 시작됨!(s번 곱한 곳 까지 제외한 후 반복길이 구하기)
#     # print(r)
#     if r != 0:
#         print(lst[s+r-1])
#     else:
#         print(lst[s+repeat_len-1]) # 반복의 맨 마지막
#
#
#
# # lst_set의 길이가 B가 된 경우
# elif len(lst_set)==B:
#     print(lst[-1])
#
# # print(lst)



# dictionary 이용. 위 방법 개선
#
# A, B, C = map(int,input().split())
# temp = A
# multi_dict = {}
#
# multiple = A
# i = 1  # 곱한 횟수
# while A not in multi_dict :
#     A %= C
#     multi_dict[A] = i
#
#     A *= multiple
#     A %= C
#     if i==B:
#         break
#
#     i += 1
#
# # 1. B번 곱한 경우
# if i == B:
#     print(multi_dict[i])
#
# # 2. B번 덜 곱한 경우
# else:
#     # a1 : 1, a2 : 2, a3 : 3, ...
#     # 현재 A가 이미 multi_dict에 있음. 즉 A는 루프의 첫 원소
#     start = multi_dict[A]   # start 번 곱하면, 루프의 첫 원소
#     # i : i번 곱하면 다시 루프의 첫원소이므로 루프의 길이는 i - start
#     length = i - start
#
#     loc = (B - start+1)%length  # 반복되는 숫자 loop에서 순서
#     # print('length is', length)
#     # print('loc is ', loc)
#     # print('start is ', start)
#     # print('temp is ', temp)
#     print(temp**(start+loc-1)%C)
# # print(multi_dict)





# 재귀방법
A, B, C = map(int,input().split())
# 예를 들어 2**64 = (2**32)**2 = ((2**16)**2)**2 = ... 꼴로 계속 반복해 나가는 것
def f(a,b,c):
    if b == 1:
        return a%c

    reduced = f(a,b//2,c)

    if b%2==0:
        return (reduced**2)%c
    else:
        return ((reduced**2)*a)%c

result = f(A,B,C)
print(result)