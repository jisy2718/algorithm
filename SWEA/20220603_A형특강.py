
# def run(n):
#     print(n, end='')
#     if n==0:
#         return
#
#     run(n-1)
#     print(n, end='')
# run(5)
# #54321012345


#
# def run2(n):
#     print(n, end='')
#     if n == 15:
#         print(n,end='')
#         return
#
#     run2(n+2)
#     print(n, end='')
# run2(3)

#
#
# def run2_prof(n):
#     if n == 17:
#         print()
#         return
#
#     print(n, end='')
#     run2_prof(n+2)
#     print(n, end='')
# run2_prof(3)


#
# def run3(n):
#     if n==2:
#         return
#
#     for i in range(2):
#         print(n, end='')
#         run3(n+1)
#         print(n,end='')
# run3(0)



# path 연습
# path=[0]*4
# def run4(level):
#     if level==2:
#         for i in range(level):
#             print(path[i], end='')
#         print()
#         return
#
#     for i in range(2):
#         path[level] = i
#         run4(level+1)
#         path[level] = 0
# run4(0)


# path 연습
# path =[0]*4
# def run5(level):
#     if level==4:
#         for i in range(level):
#             print(path[i], end='')
#         print()
#         return
#
#     for i in range(3):
#         path[level] = i+1
#         run5(level+1)
#         path[level] = 0
# run5(0)
#
#
#
# # 주사위문제
# path =[0]*10
# n = 3
# def bbq(level, sum):
#     global path, n
#     if level==n:
#         for i in range(level):
#             print(path[i], end=' ')
#         print("=" + str(sum))
#         return
#
#     for i in range(6):
#         path[level] = i+1
#         bbq(level+1, sum+i+1)
#         path[level] = 0
# bbq(0,0)



print(len(str(000)))
print(str(000))