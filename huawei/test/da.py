from datetime import datetime

#  输入:week, day表示第几周周几
#  输出:是几号
year, month, week, day = 2018, 2, 3, 1
if week > 4:
    print(0)
else:
    corr = dict(zip(range(1, 8), range(1, 8)))
    start_wd = 0
    first_sat = 0
    for d in range(1, 32):
        try:
            time_stamp = '%04d-%02d-%02d' % (year, month, d)
            d1 = datetime.fromisoformat(time_stamp)
            wd = d1.isoweekday()
            if d <= 7:
                corr[d] = wd
                if d1 == 6:
                    first_sat = d
            # 根据周几wd和号数d判断是否匹配
            if wd == day:  # 如果匹配
                print(time_stamp)
                break
        except:
            print(0)
            break
