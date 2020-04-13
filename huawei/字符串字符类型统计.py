while True:
    try:
        string = input()
        count = dict(zip(['alpha', 'space', 'digit', 'other'], [0 for _ in range(4)]))
        for s in string:
            if s.isalpha():
                count['alpha'] += 1
            elif s.isspace():
                count['space'] += 1
            elif s.isdigit():
                count['digit'] += 1
            else:
                count['other'] += 1
        print(count['alpha'])
        print(count['space'])
        print(count['digit'])
        print(count['other'])
    except:
        break
