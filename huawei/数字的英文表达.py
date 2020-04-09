# def convert_num(s):
#     mapping1 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#     mapping2 = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
#     r = ''
#     if len(s) == 3:  # 长度为3且
#         r += ' '
#         if int(s[0]):  # 最高位不为0的情况
#             r += mapping1[int(s[0])]
#             r += ' hundred'
#             if not s[1:] == '00':
#                 r += ' and'
#         # if s[0] == '0' and s != '000':  # 最高位为0的情况
#         #     r += 'and'
#         r += ' '
#     if len(s) >= 2 and s[-2:] in ['11', '12']:
#
#         r += 'eleven' if s[-2:] == '11' else 'twelve'
#         r += ' '
#         return r
#     if len(s) >= 2 and s[-2:] == '10':
#         r += 'ten'
#         r += ' '
#         return r
#     if len(s) >= 2 and int(s[-2]):  # 长度为2且第二位不为0
#         r += mapping2[int(s[-2])]
#         r += ' '
#     if len(s) >= 1 and int(s[-1]):  # 长度为2且最后一位不为0
#         r += mapping1[int(s[-1])]
#         r += ' '
#     return r
#
#
# def convert(s):
#     result = ''
#     if len(s) > 9:
#         result += convert(s[:-9])
#         result += 'billion'
#     if len(s) > 6:
#         result += convert_num(s[-9:-6])
#         if not s[-9:-6] == '000':
#             result += 'million'
#     if len(s) > 3:
#         result += convert_num(s[-6:-3])
#         if not s[-6:-3] == '000':
#             result += 'thousand'
#     result += convert_num(s[-3:])
#     return result
#
#
# while True:
#     try:
#         num = input().strip()
#         result = ''
#         if len(num) > 9:
#             result += convert(num[:-9])
#             result += 'billion'
#         result += convert(num[-9:])
#         print(result.strip())
#     except:
#         break

# https://www.nowcoder.com/profile/8700811/codeBookDetail?submissionId=12483596


def transfer(n):
    a1 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
          'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    a2 = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    result = ""
    if n // 10 ** 2 != 0:
        result += a1[n // 10 ** 2] + " hundred "
        if n % 10 ** 2 != 0:
            result += "and "
    if n % 10 ** 2 >= 20:
        result += a2[(n % 10 ** 2) // 10]
        if n % 10 != 0:
            result += " " + a1[n % 10]
    else:
        result += a1[n % 10 ** 2]
    return result


while True:
    try:
        n = int(input().strip())
        result = ""
        if n // 10 ** 6 != 0:
            result += transfer(n // 10 ** 6) + " million "
        if n // 10 ** 3 != 0:
            result += transfer((n % 10 ** 6) // 10 ** 3) + " thousand "
        result += transfer(n % 10 ** 3)
        print(result)
    except:
        break
