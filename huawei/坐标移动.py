import re

while True:
    try:
        coordinate = [0, 0]
        moves = input().strip().split(';')
        for m in reversed(moves):
            if not re.match(r'^(A|W|S|D){1}[0-9]{1,2}$', m):
                moves.remove(m)
        for m in moves:
            direction = m[0]
            distance = int(m[1:])
            if direction == 'A':
                coordinate[0] -= distance
            elif direction == 'W':
                coordinate[1] += distance
            elif direction == 'S':
                coordinate[1] -= distance
            else:
                coordinate[0] += distance
        print(','.join(map(str, coordinate)))
    except:
        break