import sys
import math

num = input()

for index, i in enumerate(num.split()):
    len_num = len(i)
    answer = 0
    for j in i:
        now = math.factorial(int(len_num))
        answer += now * int(j)
        len_num -= 1
    if index == 4:
        print(answer, end='')
        break
    print(answer)
