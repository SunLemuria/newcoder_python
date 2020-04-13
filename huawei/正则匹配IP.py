import re


while True:
    try:
        mask = input().strip()
        ip1 = input().strip()
        ip2 = input().strip()
        mask_pattern = r'^(255\.)(255\.|0.){2}0$'
        ip_pattern = r'^(([01][0-9][0-9]?|25[0-5]|2[0-4][0-9])\.){3}([01][0-9][0-9]?|25[0-5]|2[0-4][0-9])$'
        if not (re.match(mask_pattern, mask) or re.match(ip_pattern, ip1) or re.match(ip_pattern, ip2)):
            print('1')
            break
        ma = mask.strip().split('.')
        i1 = ip1.strip().split('.')
        i2 = ip2.strip().split('.')
        for i in range(4):
            if ma[i] == '255':
                if i1[i] != i2[i]:
                    print('2')
                    break
        else:
            print('0')

    except:
        break