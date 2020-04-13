import re


while True:
    try:
        mask, ip1, ip2 = tuple(input().strip().split())
        mask_pattern = r'(255\.){3}\.0'
        # ip_pattern = r'(([01]?[0-9][0-9]?|25[0-5]|2[0-4][0-9])\.){3}([01]?[0-9][0-9]?|25[0-5]|2[0-4][0-9])'
        ip_pattern = r'^(\d{1, 2}|1\d\d|2[0-4]\d|25[0-5])(\.(\d{1, 2}|1\d\d|2[0-4]\d|25[0-5])){3}$'
        if not re.match(mask_pattern, mask) or re.match(ip_pattern, ip1) or re.match(ip_pattern, ip2):
            print('1')
            break
        if ip1[0:ip1.rfind('.')] == ip2[0:ip2.rfind('.')]:
            print('0')
        else:
            print('2')
    except:
        break