# 猫狗队列 【题目】 宠物、狗和猫的类如下：
# public class Pet { private String type;
# public Pet(String type) { this.type = type; }
# public String getPetType() { return this.type; }
# }
# public class Dog extends Pet { public Dog() { super("dog"); } }
# public class Cat extends Pet { public Cat() { super("cat"); } }
# 实现一种狗猫队列的结构，要求如下： 用户可以调用add方法将cat类或dog类的
# 实例放入队列中； 用户可以调用pollAll方法，将队列中所有的实例按照进队列
# 的先后顺序依次弹出； 用户可以调用pollDog方法，将队列中dog类的实例按照
# 进队列的先后顺序依次弹出； 用户可以调用pollCat方法，将队列中cat类的实
# 例按照进队列的先后顺序依次弹出； 用户可以调用isEmpty方法，检查队列中是
# 否还有dog或cat的实例； 用户可以调用isDogEmpty方法，检查队列中是否有dog
# 类的实例； 用户可以调用isCatEmpty方法，检查队列中是否有cat类的实例。


class AddPet(object):
    count = 0
    dogs = dict()
    cats = dict()
    all_count = list()
    dogs_count = list()
    cats_count = list()

    @classmethod
    def addDogs(cls, name):
        cls.dogs[cls.count] = name
        cls.dogs_count.append(cls.count)
        cls.all_count.append(cls.count)
        cls.count += 1
        print(cls.dogs)

    @classmethod
    def addCats(cls, name):
        cls.cats[cls.count] = name
        cls.cats_count.append(cls.count)
        cls.all_count.append(cls.count)
        cls.count += 1
        print(cls.cats)

    @classmethod
    def pullAll(cls):
        try:
            firstly = cls.dogs[cls.all_count[0]]
            cls.dogs.pop(cls.all_count[0])
            print(firstly)
        except Exception as e:
            pass
        try:
            firstly = cls.cats[cls.all_count[0]]
            cls.cats.pop(cls.all_count[0])
            print(firstly)
        except Exception as e:
            pass
        cls.all_count.pop(0)

    @classmethod
    def pollDog(cls):
        fist_dog = cls.dogs[cls.dogs_count[0]]
        cls.all_count.remove(cls.dogs_count[0])
        cls.dogs_count.pop(0)
        print(fist_dog)

    @classmethod
    def pollCat(cls):
        fist_cat = cls.cats[cls.cats_count[0]]
        cls.all_count.remove(cls.cats_count[0])
        cls.cats_count.pop(0)
        print(fist_cat)


pets = AddPet()
pets.addCats('cat1')
pets.addDogs('dog1')
pets.addDogs('dog2')
pets.addCats('cat2')
pets.addCats('cat3')
pets.addDogs('dog3')
pets.pollCat()
pets.pollCat()
pets.pullAll()
pets.pullAll()
pets.pullAll()
pets.pullAll()
