while True:
    try:
        s = input().strip()
        sorted_s = sorted(s, key=lambda x: ord(x.lower()))
        sorted_alphas = list(filter(lambda x: x.isalpha(), sorted_s))
        result = ''
        j = 0
        for i in range(len(s)):
            if not s[i].isalpha():
                result += s[i]
            else:
                result += sorted_alphas[j]
                j += 1
        print(result)
    except:
        break
