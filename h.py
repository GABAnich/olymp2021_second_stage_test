str_input = input()

arr = str_input.split(' ')

for i in range(1, len(arr)):
    arr[i] = arr[i].capitalize()

print("".join(arr))
