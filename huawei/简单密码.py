while True:
    try:
        encoded_pd = input().strip()
        real_pd = ''
        encoded_char = ''
        for p in encoded_pd:
            if p.isupper():
                lower = chr(ord(p.lower()) + 1)
                encoded_char = lower if lower.isalpha() else 'a'
            elif p.islower():
                if p in 'abc':
                    encoded_char = '2'
                elif p in 'def':
                    encoded_char = '3'
                elif p in 'ghi':
                    encoded_char = '4'
                elif p in 'jkl':
                    encoded_char = '5'
                elif p in 'mno':
                    encoded_char = '6'
                elif p in 'pqrs':
                    encoded_char = '7'
                elif p in 'tuv':
                    encoded_char = '8'
                else:
                    encoded_char = '9'
            else:
                encoded_char = p
            real_pd += encoded_char
        print(real_pd)
    except:
        break