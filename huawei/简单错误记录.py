import sys

d = {}
names = []

while True:
    try:
        v = input().split()
        name = v[0].split('\\')[-1]

        if len(name) >= 16:
            name = name[-16:]

        line = name + ' ' + str(v[-1])
        if line not in d:
            names.append(line)
            d[line] = 1
        else:
            d[line] += 1
    except:
        break

for item in names[-8:]:
    sys.stdout.write(item + ' ' + str(d[item]) + '\n')
