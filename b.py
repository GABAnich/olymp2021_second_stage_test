[n, m] = input().split(' ')
n = int(n)
m = int(m)
arr = [['.' for x in range(m)] for y in range(n)] 

[x, y] = input().split(' ')
x = int(x)
y = int(y)
arr[x - 1][y - 1] = '*'

k = int(input())
for i in range(k):
    [direction, count] = input().split(' ')
    count = int(count)
    for i in range(count):
        if direction == 'U':
            x -= 1
        elif direction == 'D':
            x += 1
        elif direction == 'L':
            y -= 1
        elif direction == 'R':
            y += 1
        arr[x - 1][y - 1] = '*'



for row in arr:
    for col in row:
        print(col, end='')
    print()
