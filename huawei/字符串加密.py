while True:
    try:
        key = input().strip()
        data = input().strip()
        remain = ''
        for k in key.upper():  # key去重
            if k not in remain:
                remain += k
        for code in range(65, 91):  # 字母转换
            if chr(code) not in remain:
                remain += chr(code)
        mapping = dict(zip([chr(code) for code in range(65, 91)], list(remain)))
        encrypt = ''
        for s in data:
            if not s:  # 空格直接添加
                encrypt += s
            if s not in mapping:  # 小写
                encrypt += mapping[s.upper()].lower()
            else:
                encrypt += mapping[s]   # 大写
        print(encrypt)
    except:
        break