n = int(input())

max_tree = -1
max_high = -1

tree = 1
for i in range(n):
    branches = input().split(' ')
    branches.pop(0)

    res = max([int(num) for num in branches])
    if (res >= max_high):
        max_high = res
        max_tree = i + 1


print("{} {}".format(max_tree, max_high))
