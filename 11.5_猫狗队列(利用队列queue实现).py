"""
思路：
建立一个猫的类 里面存放这只猫的ID一个类属性 同样的建立一个狗的类
一个add类 里面用队列的方式存储想要加入的具体的狗或者猫的对象 以及一个count时间戳类属性用来存放不论猫还是狗对象进队列的时间戳
同时这个add类里有两个队列 一个猫队列一个狗队列 pollDog方法可以从狗队列取出一个狗对象 pollCat从猫队列取出猫对象
pollPet方法取出add类里时间戳属性较大的那一个对象
isEmpty、isDogEmpty与isCatEmpty分别可以查看队列中是否为空
"""
import queue


class Cat(object):
    def __init__(self, name):
        self.name = name


class Dog(object):
    def __init__(self, name):
        self.name = name


class Add(object):
    count = 0
    q_cat = queue.LifoQueue()
    q_dog = queue.LifoQueue()

    def add(self, pet):
        Add.count += 1
        self.pet = pet
        self.pet.count = Add.count
        print(self.pet)
        # if type(self.pet) == "<class '__main__.Dog'>":
        if 'Dog' in str(type(self.pet)):
            self.dogInDogQueue()
        else:
            self.catInCatQueue()

    def catInCatQueue(self):
        Add.q_cat.put(self.pet)

    def dogInDogQueue(self):
        Add.q_dog.put(self.pet)

    def pollCat(self):
        if not Add.q_cat.empty():
            print(Add.q_cat.get().name)
        else:
            ex = Exception('猫队列为空')
            raise ex

    def pollDog(self):
        if not Add.q_dog.empty():
            print(Add.q_dog.get().name)
        else:
            ex = Exception('狗队列为空')
            raise ex

    def pollPet(self):
        last_cat = Add.q_cat.get()
        last_dog = Add.q_dog.get()
        if last_cat.count > last_dog.count:
            print(last_cat.name)
            Add.q_dog.put(last_dog)
        else:
            print(last_dog.name)
            Add.q_cat.put(last_cat)

    def isCatEmpty(self):
        print(Add.q_cat.empty())

    def isDogEmpty(self):
        print(Add.q_dog.empty())

    def isEmpty(self):
        print(Add.q_cat.empty() and Add.q_dog.empty())

dog1 = Dog('dog1')
dog2 = Dog('dog2')
cat1 = Cat('cat1')
cat2 = Cat('cat2')
dog3 = Dog('dog3')
cat3 = Cat('cat3')
text = Add()
text.add(dog1)
text.add(dog2)
text.add(cat1)
text.add(cat2)
text.add(dog3)
text.add(cat3)
text.pollDog()
text.pollPet()
text.pollCat()
text.pollPet()
# text.q_cat.get()
