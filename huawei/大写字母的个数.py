while True:
    try:
        string = input().strip()
        print(len(list(filter(lambda x: x.isupper(), string))))
    except:
        break
