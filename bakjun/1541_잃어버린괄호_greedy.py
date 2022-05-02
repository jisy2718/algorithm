# 음수로 만들 수 있는 것들은, 음수로 다 만들면 됨
# - 가 한 번 나오기 시작하면, 그 뒤의 수는 모두 음수로 만들 수 있음



L = input()


# split 해서 음수인 부분과 아닌 부분 나눌 수 있음
# L = '-53+20' => L.split('-') = ['', '53+20']
# L='15-53+20-30+2'=> L.split('-') = ['15', '53+20', '30+2']
# L = '50+1' = ['50+1']
# 즉 split 된 맨 앞 수들에서, 그 뒤의 모든 수들을 빼면 됨



splitL = L.split('-')

# plus와 minuss 의 원소들은 모두 '10+3' or '10' 꼴로, + 연산자가 있는  str임.
plus = splitL[0]
minuss = splitL[1:]

plus_list = list(map(int,plus.split('+')))

minus_list = []

for minus in minuss:
    minus_list += list(map(int,minus.split('+')))


plus_sum = 0
minus_sum = 0

for num in plus_list:
    plus_sum += num

for num in minus_list:
    minus_sum += num

print(plus_sum-minus_sum)
