# a+b+c=1000 a^2+b^2=c^2 求出abc的所有组合可能
import time


def demo():
    start_time = time.time()
    for a in range(1, 1001):
        for b in range(1, 1001):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                print(a, b, c)
    end_time = time.time()
    print('times:%.2f' % (end_time - start_time))

demo()



# def demo2():
#     for a in range(1, 1001):
#         b + c = 1000 - a
#         a ** 2 + b ** 2 = c ** 2
#         print(a, b, c)
#
#
# demo2()