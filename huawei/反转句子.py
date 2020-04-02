while True:
    try:
        sentence = input().split()
        for word in reversed(sentence):
            print(word, end=' ')
    except:
        break