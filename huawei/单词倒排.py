while True:
    try:
        sentence = input().strip()
        string = ''
        for s in sentence:
            to_append = s if s.isalpha() else ' '  # 非字母的处理
            string += to_append
        word_list = string.split()
        print(' '.join(reversed(word_list)))
    except:
        break