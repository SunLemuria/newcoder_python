import heapq

while True:
    try:
        n, k = tuple(map(int, input().split()))
        nums = list(map(int, input().split()))
        heapq.heapify(nums)
        k_smallest = heapq.nsmallest(k, nums)
        print(' '.join(list(map(str, k_smallest))))
    except:
        break
