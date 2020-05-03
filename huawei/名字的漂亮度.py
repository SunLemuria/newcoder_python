while True:
    try:
        n = int(input().strip())
        name_list = []
        for _ in range(n):
            name = input().strip()
            name_set = set(name)
            count = [name.count(x) for x in name_set]
            count.sort(reverse=True)

            total = sum((26 - i) * c for i, c in enumerate(count))
            print(total)
    except:
        break
