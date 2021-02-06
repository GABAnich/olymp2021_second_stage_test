res = {}

n = int(input())
for i in range(n):
    str_input = input()
    [sender, reciever] = str_input.split(' ')

    if (reciever not in res):
        res[reciever] = []
    res[reciever].append(sender)

keys = list(res.keys())
keys.sort()

for k in keys:
    print("{} {}".format(k, len(res[k])))
    sendersDict = {}
    for s in res[k]:
        sendersDict[s] = s

    senders = list(sendersDict.values())
    senders.sort()
    print(",".join(senders))
