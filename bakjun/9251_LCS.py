# a = input()
# b = input()
# N = max(len(a),len(b))
#
# s = [[0]*N for _ in range(N)]
#
#
# #    a |a b c d e f g h i j k l m l
# #  b   |
# #----- |-----------------------------
# #  a   |
# #  b   |
# #  c   |
# #  d   |
# #  ... |
# for r in range(len(b)):
#     for c in range(len(a)):
#         # 현재 글자가 일치한다면, 두 수열 모두에서 바로 앞까지 최대길이 + 1
#         if b[r] == a[c]:
#             s[r][c] = s[r-1][c-1]+1 if r >0 and c >0 else 1
#
#         # 현재 글자가 일치하지 않는다면
#         # a[:c]와 b[:r+1] 사이의 최대 공통 수열과 a[:c+1]과 b[:r] 사이의 최대 공통 수열중 큰 것과 같음
#         else:
#             s[r][c] = max(s[r-1][c],s[r][c-1]) if r > 0 and c >0 else 0
#
# for row in s:
#     print(row)
# print(s[len(b)-1][len(a)-1])
#
#



#-------------------------------------------------------
a = input()
b = input()
N = max(len(a),len(b))

s = [[0]*(N+1) for _ in range(N+1)]


#    a |a b c d e f g h i j k l m l
#  b   |
#----- |-----------------------------
#  a   |
#  b   |
#  c   |
#  d   |
#  ... |
for r in range(1,len(b)+1):
    for c in range(1,len(a)+1):
        # 현재 글자가 일치한다면, 두 수열 모두에서 바로 앞까지 최대길이 + 1
        if b[r-1] == a[c-1]:
            s[r][c] = s[r-1][c-1]+1

        # 현재 글자가 일치하지 않는다면
        # a[:c]와 b[:r+1] 사이의 최대 공통 수열과 a[:c+1]과 b[:r] 사이의 최대 공통 수열중 큰 것과 같음
        else:
            s[r][c] = max(s[r-1][c],s[r][c-1])


print(s[len(b)][len(a)])


