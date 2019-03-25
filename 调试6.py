# a = {1: [10, 20], 2: [20, 30], 3: [30, 40]}
# b = [{1: [10, 20]}, {2: [20, 30]}, {3: [30, 40]}]
# print(list(b[0].values()))

# a = []
# if a != None:
#     print(True)
# else:
#     print(False)

# import datetime
#
# t1 = datetime.time(10, 20)
# t2 = datetime.time(10, 30)
# t4 = '10:20'
# print(t1 < t2)
# t3 = t4.replace(':', '')
# print(t3)


def sort(arr, num):
    left = 0
    right = len(arr) - 1
    mid = left + ((right - left) >> 1)
    # print(mid)
    while num <= arr[-1]:
        if num < arr[mid]:
            right = mid - 1
            mid = left + ((right - left) >> 1)
        elif num > arr[mid]:
            left = mid + 1
            mid = left + ((right - left) >> 1)
        else:
            return mid


res = sort([1, 2, 3, 4, 5, 6, 7, 8], 7)
print(res)


def stackFind(arr, num, left, right):
    mid = left + ((right - left) >> 1)
    if arr[mid] == num:
        return mid
    if arr[mid] < num:
        return stackFind(arr, num, mid + 1, right)
    elif arr[mid] > num:
        return stackFind(arr, num, left, mid - 1)


res = stackFind([1, 2, 3, 4, 5, 6, 7, 8], 7, 0, 7)
print(res)


def base(arr, num):
    length = len(arr) - 1
    return quickFind(arr, num, length)


def quickFind(arr, num, length):
    count = length >> 1
    mid = len(arr) - 1 >> 1
    if arr[mid] == num:
        return count
    if arr[mid] < num:
        length += mid + 1
        return quickFind(arr[mid + 1:], num, length)
    elif arr[mid] > num:
        length -= mid + 1
        return quickFind(arr[: mid], num, length)


res = base([1, 2, 3, 4, 5, 6, 7, 8, 9], 1)
print(res)
