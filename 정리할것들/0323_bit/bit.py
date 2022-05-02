# 0000000111100000011000000111100110000110000111100111100111111001100111

bits = list(map(int,input()))

print(len(bits))
result = []
bit_result = []
for i in range(0,len(bits),7):
    target = bits[i:i+7]
    num = 0
    for j in range(1,8):
        num += target[-j]*2**(j-1)
    result.append(num)
    bit_result.append(target)


print(result)
print(bit_result)
import sys
print(sys.byteorder)