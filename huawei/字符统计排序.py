# while True:
#     try:
#         string = input().strip()
#         buckets = [[] for _ in range(len(string))]
#         d = dict()
#         for s in string:
#             if s not in d:
#                 d[s] = 1
#             else:
#                 d[s] += 1
#         for k, v in d.items():
#             buckets[v].append(k)
#         result = ''
#         for bucket in reversed(buckets):
#             if len(bucket):
#                 bucket.sort()
#                 for units_decimal in bucket:
#                     result += units_decimal
#         print(result)
#     except:
#         break

while True:
    try:
        string = input().strip()
        d = {}
        for s in string:
            if s.isdigit() or s.isalpha() or s == ' ':
                if s in d.keys():
                    d[s] += 1
                else:
                    d[s] = 1
        # 先按字母升序, 后按个数降序
        d2 = sorted(sorted(d.items(), key=lambda x: x[0]), key=lambda item: item[1], reverse=True)
        str1 = ''.join([k for (k, v) in d2])
        print(str1)
    except:
        break
