[n, m] = [int(e) for e in input().split(' ')]

res = []
dep = {}
for k in range(n):
    dep[k + 1] = "av"

arr = [0 for i in range(m)]
for i in range(m):
    [a, b] = [int(e) for e in input().split(' ')]
    arr[i] = [a, b] 

for el in arr:
    dep[el[1]] = "un"

def get_av():
    res = []
    for k in list(dep.keys()):
        if dep[k] == "av":
            res.append(k)
    return res

def get_av_from_k(k):
    res = []
    for i in range(len(arr)):
        if arr[i][0] == k:
            res.append(arr[i][1])
    return res


while len(get_av()) > 0:
    av = get_av()
    for k in av:
        dep[k] = "finished"
        if k not in res:
            res.append(k)
        new_av = get_av_from_k(k)
        for e in new_av:
            dep[e] = "av"

if (len(res) > 0):
    print("Yes")
    print(" ".join("{}".format(n) for n in res))
else:
    print("No")
