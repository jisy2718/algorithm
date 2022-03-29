def make_post(expression):
    # -------------후위표기-------------------
    # 1. icp, isp, post, stack
    icp = {'+': 1, '*': 2, '(': 3}
    isp = {'+': 1, '*': 2, '(': 0}
    post = ''
    stack = []

    for element in expression:
        # 2. 연산자, ( 인 경우

        if element in '+*(':
            if not stack:
                stack.append(element)
            else:

                if isp[stack[-1]] < icp[element]:
                    stack.append(element)
                else:
                    while stack and isp[stack[-1]] >= icp[element]:
                        post += stack.pop()
                    # 자신보다 작아지면 push
                    stack.append(element)

        # 3. 닫는괄호경우
        elif element == ')':
            while stack[-1] != '(':
                post += stack.pop()
            # '(' 가 나온경우 그냥 pop
            stack.pop()

        # 4. 숫자 경우
        else:
            post += element

        # print(f"stack is {stack}")
        # print(f"post is {post}")

    # ------------------------후위표기 계산-----------
    stack2 = []
    # stack2에 넣을 때 정수로 변환해서 넣기
    for element in post:
        # 연산자 경우
        if element in '+*':
            back = stack2.pop()
            front = stack2.pop()
            if element == '+':
                stack2.append(front + back)
            else:
                stack2.append(front * back)

        # 숫자경우
        else:
            stack2.append(int(element))

    print(f'#{tc} {stack2[-1]}')


for tc in range(1, 11):
    N = int(input())
    exp = input()
    make_post(exp)