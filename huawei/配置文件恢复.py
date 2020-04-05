import sys


def checkTwoKeys(twoKeys, a, result):
    count = 0
    index = 0
    for y in twoKeys:
        if y.split()[0].startswith(a[0]) and y.split()[1].startswith(a[1]):
            count += 1
            index = twoKeys.index(y)
    if count > 1 or count == 0:
        print("unkown command")
    elif count == 1:
        print(result[index])


oneKey = 'reset'
twoKeys = ['reset board', 'reboot backplane', 'backplane abort', 'board add', 'board delete']
result = ['board fault', 'impossible', 'install first', 'where to add', 'no board at all']
line = [cmd for cmd in sys.stdin]
for x in line:
    cmd = x.strip().split()
    l = len(cmd)
    if l <= 0 or l >= 3:
        print("unkown command")
    elif l == 1:
        if 'reset'.startswith(cmd[0]):
            print("reset what")
        else:
            print("unkown command")
    elif l == 2:
        checkTwoKeys(twoKeys, cmd, result)
