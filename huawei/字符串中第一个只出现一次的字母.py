while True:
    try:
        string = input()
        candidates = []
        already_exists = []
        for s in string:
            if s not in candidates and s not in already_exists:
                candidates.append(s)
            else:
                if s in candidates:
                    candidates.remove(s)
                if s not in already_exists:
                    already_exists.append(s)
        print(candidates[0] if candidates else -1)
    except:
        break
