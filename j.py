n = int(input())

input_arr = []
for i in range(n):
    str_input = input()
    input_arr.append(str_input)

input_arr.sort()

sum = 0
for i in range(len(input_arr)):
    tmp_sum = 0
    for s in input_arr[i]:
        tmp_sum += ord(s) - 64
    sum += tmp_sum * (i + 1)

print(sum)
