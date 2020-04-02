while True:
    try:
        string = input()
        print(''.join(list(reversed(string))))
    except:
        break