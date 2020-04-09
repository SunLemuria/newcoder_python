while True:
    try:
        string = input().strip()

        sign = False
        result = {}
        digit_string = ''
        length = 0
        for s in string:
            is_digit = s.isdigit()
            # 类型变化,从数字变为非数字或从非数字变为数字
            if is_digit ^ sign:
                sign = is_digit
                if digit_string:  # 从数字变为非数字时digit_string不为空
                    if length not in result:
                        result[length] = [digit_string]
                    else:
                        if digit_string not in result[length]:
                            result[length].append(digit_string)
                    length = 0
            if is_digit:  # 从非数字变为数字或一直为数字时加入到digit_string中
                digit_string += s
                length += 1
            else:  # 从数字变为非数字或一直为非数字时digit_string为空
                digit_string = ''
        if string[-1].isdigit():
            if digit_string:
                if length not in result:
                    result[length] = [digit_string]
                else:
                    if digit_string not in result[length]:
                        result[length].append(digit_string)
        sorted_result = sorted(result.items(), key=lambda x: x[0], reverse=True)
        longest = sorted_result[0]
        print_format = ''.join(longest[1])
        print_format += ',%d' % longest[0]
        print(print_format)

    except:
        break