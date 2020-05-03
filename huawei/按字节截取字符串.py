# https://www.nowcoder.com/practice/a30bbc1a0aca4c27b86dd88868de4a4a?tpId=37&tqId=21269&rp=0&ru=/ta/huawei&qru=/ta/huawei/question-ranking

while True:
    try:
        st = input().strip()
        n = int(st.split()[-1])
        # n = int(input().strip())
        count = 0
        index = 0
        last_count = 0
        for i, s in enumerate(st):
            last_count = 1 if ord(s) < 123 else 2  # 用isalpha()不能区分汉字，要用ASCII码区分
            count += last_count
            index = i + 1
            if count >= n:
                break
        if last_count == 2:
            index -= 1
        print(st[:index])
    except:
        break
