while True:
    try:
        num_candidates = int(input().strip())
        candidates = input().strip().split()

        num_votes = int(input().strip())
        votes = input().strip().split()

        result = dict(zip(candidates, [0 for _ in range(num_candidates)]))

        invalid = 0
        for v in votes:
            if v in result:
                result[v] += 1
            else:
                invalid += 1
        for k, v in result.items():
            print(k, ':', v)
        # for name in candidates:
        #     print('%s : %d' % (name, result.get(name)))
        print('Invalid :', invalid)
    except:
        break


while True:
    try:
        num_candidates = int(input().strip())
        candidates = input().strip().split(' ')

        num_votes = int(input().strip())
        votes = input().strip().split(' ')

        result = dict(zip(candidates, [0 for _ in range(num_candidates)]))

        invalid = 0
        for v in votes:
            if v in result:
                result[v] += 1
            else:
                invalid += 1
        for name in candidates:
            print('%s : %d' % (name, result.get(name)))
        print('Invalid : %d' % invalid)
    except:
        break