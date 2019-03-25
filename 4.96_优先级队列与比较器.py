# student1 = {'name': 'A', 'id': 1, 'age': 23}
# student2 = {'name': 'B', 'id': 2, 'age': 21}
# student3 = {'name': 'C', 'id': 3, 'age': 22}
# students = [('john', 'A', 15), ('jane', 'B', 12), ('dave','B', 10)]


# class Student(object):
#     def __init__(self, string_name, identity, age):
#         self.string_name = string_name
#         self.identity = identity
#         self.age = age
#
#
# def compare(o1, o2):
#     if o1.identity < o2.identity:
#         return -1
#     elif o1.identity > o2.identity:
#         return 1
#     else:
#         return 0


# student1 = Student("A", 1, 23)
# student2 = Student("B", 2, 21)
# student3 = Student("C", 3, 22)
# students = [student1, student2, student3]
# students.sort(key=compare)


# students = [('john', 'A', 15), ('jane', 'B', 12), ('dave','B', 10)]
# print(sorted(students, key=lambda x: x[2]))  # 按照年龄来排序


import queue as Q


class Skill(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description

    def __lt__(self, other):
        if self.priority < other.priority:
            return True

    def __str__(self):
        return '(' + str(self.priority) + ',\'' + self.description + '\')'


def PriorityQueue_class():
    que = Q.PriorityQueue()
    que.put(Skill(7, 'proficient7'))
    que.put(Skill(5, 'proficient5'))
    que.put(Skill(6, 'proficient6'))
    que.put(Skill(10, 'expert'))
    que.put(Skill(1, 'novice'))
    print('end')
    while not que.empty():
        print(que.get())


PriorityQueue_class()

'''
当队列的元素是自定义时，需要我们在元素的类中定义出比较规则
优先级队列本身就是一个堆
'''