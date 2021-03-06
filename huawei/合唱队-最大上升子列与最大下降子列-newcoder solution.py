# def lower_bound(nums, target):
#     low, high = 0, len(nums) - 1
#     pos = len(nums)
#     while low < high:
#         mid = int((low + high) / 2)
#         if nums[mid] < target:
#             low = mid + 1
#         else:
#             high = mid
#             pos = high
#     return pos
#
#
# def deal(l, res):
#     b = [9999] * len(l)
#     b[0] = l[0]
#     res = res + [1]
#     for i in range(1, len(l)):
#         pos = lower_bound(b, l[i])
#         # pos = b.index(l[i])
#         res += [pos + 1]
#         b[pos] = l[i]
#     return res
#
#
# while True:
#     try:
#         n = int(input())
#         q = [int(i) for i in input().strip().split()]
#         dp_1 = []
#         dp_2 = []
#         dp_1 = deal(q, dp_1)
#         q.reverse()
#         dp_2 = deal(q, dp_2)
#         dp_2.reverse()
#         a = max([dp_1[i] + dp_2[i] for i in range(n)])
#         print(n - a + 1)
#     except:
#         break


import bisect

while True:
    try:
        n = int(input())
        list1 = [int(i) for i in input().split()]


        def find_sort_arr(l1, num):
            arr = [99999999] * num
            arr[0] = l1[0]
            res = []
            res += [1]
            for i in range(1, len(l1)):
                pos = bisect.bisect_left(arr, l1[i])
                res.append(pos + 1)
                arr[pos] = l1[i]
            return res


        res1 = find_sort_arr(list1, n)
        res2 = find_sort_arr(list1[::-1], n)[::-1]
        result_arr = list(map(lambda x, y: x + y, res1, res2))
        print(n - (max(result_arr) - 1))
    except:
        break
