import re

while True:
    try:
        ip = input().strip()
        result = re.match(
            r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ip)
        print('YES') if result else print('NO')
    except:
        break
