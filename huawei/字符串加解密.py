def encrypt(raw):
    result = ''
    for s in raw:
        if s.islower():
            st = chr(ord(s) + 1)
            result += st.upper() if st.islower() else 'A'
        elif s.isupper():
            st = chr(ord(s) + 1)
            result += st.lower() if st.isupper() else 'a'
        elif s.isdigit():
            result += str(int(s) + 1) if int(s) < 9 else '0'
        else:
            result += s
    return result


def unencrypt(encrypted):
    result = ''
    for s in encrypted:
        if s.islower():
            st = chr(ord(s) - 1)
            result += st.upper() if st.islower() else 'Z'
        elif s.isupper():
            st = chr(ord(s) - 1)
            result += st.lower() if st.isupper() else 'z'
        elif s.isdigit():
            result += str(int(s) - 1) if int(s) > 0 else '9'
        else:
            result += s
    return result


while True:
    try:
        raw = input().strip()
        encrypted = input().strip()
        print(encrypt(raw))
        print(unencrypt(encrypted))
    except:
        break
