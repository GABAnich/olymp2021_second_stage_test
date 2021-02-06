#  import re

#  str_input = input()
#  print(re.findall(r'\d\d\d', str_input))

####

#  str_input = input()

#  res_arr = []
#  tmp_arr = []
#  i = 0
#  for s in str_input[::-1]:
    #  i += 1
    #  print(i % 3)
    #  if i % 3 == 0:
        #  res_arr.append(tmp_arr)
        #  tmp_arr = []
        #  tmp_arr.append(s)
    #  tmp_arr.append(s)

#  print(res_arr)


str_input = input()

is_dash = False
if str_input[0] == '-':
    is_dash = True
    str_input = str_input[1::]

res = []
counter = 0
for i in range(len(str_input) - 1, -1, -1):
    if (counter != 0 and counter % 3 == 0):
        res.insert(0, ',')
    res.insert(0, str_input[i])
    counter += 1


if is_dash:
    res.insert(0, '-')

print(''.join(res))


