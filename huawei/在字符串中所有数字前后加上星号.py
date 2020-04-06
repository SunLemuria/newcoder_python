while True:
    try:
        string = input().strip()
        result = ''
        sign = False
        for s in string:
            is_digit = s.isdigit()
            if is_digit ^ sign:
                sign = is_digit
                result += '*'
            result += s
        if string[-1].isdigit():
            result += '*'
        print(result)
    except:
        break