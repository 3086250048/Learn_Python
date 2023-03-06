'''
面向对象的语言关注的时对象，不关注过程
面向对象的思想
1.找object
2.用object

-我们目前所学习的对象都是python内置的对象(int,str,list,tuple)
但是内置对象无法满足所以需求,需要自定义对象

class 简单的理解就是一张图纸，依据图纸它可以生产(实例化)一个工具箱(instance)，函数就相当于工具箱中的螺丝刀，可以用来拧螺丝，
你无需关注这把螺丝刀如何制造。使用时你需要先找到工具箱，然后才能找到螺丝刀然后去拧螺丝。
这个工具箱中还有锯子，同样你无需关注如何造锯子，你只需....
    -自定义类需要使用大驼峰命名法
    -语法
        -class 类名([父类]):
            代码块
'''
#下面这个写法，实际上就是实例化了一个int类的实例,等价于a=10
# a=int(10) 


# class Cla0():
#     pass
# #c01是Cla0类的一个实例
# c01= Cla0()
'''
<__main__.Cla0 object (通过当前py文件中的CLa0类实例化的对象)
at 0x000002291A3FFB90> (对象的地址为......)

'''
# print(c01)
# print(type(c01))

'''
isinstance()检查一个对象是否时一个类的实例。是返回true，不是返回false
'''
# print(isinstance(c01,Cla0))


'''
类实际上也是一个type类型的对象
'''
# print(id(Cla0),type(Cla0))

'''
对象实际上也是一个变量，对象中的变量称为属性
语法 对象.属性=xxx
'''
# c01.name='czz'



'''
创建一个表示人的类
'''
# class Person():
    #在类中我们可以定义变量和函数
    #在类中所定义的变量，将会成为所以实例1的公共属性
    #所以实例都可以访问这些变量
    # name='czz'#公共属性，所以实例都可以访问
    # age='18'
    #在类中定义的函数称为方法
#     def talk(self):
#         print('你好世界'+f'我是{self.name}')

# p1=Person()
# p2=Person()
# p1.name='cxc'
# p2.name='ycj'
# print(p1.name,p2.name,sep='|')

'''
调用方法的方式: 实例化对象.方法名()
方法调用和函数调用的区别
    -方法调用会默认传递一个参数由解析器自动传递，
    所以方法中至少要一个形参
    -这个自动传递的参数就是调用对象的本身

    -属性和方法查找的流程
        类中定义的属性和方法都是公共的，任何类和实例都可以访问
        当我们调用一个对象的属性时，解析器会在当前对象中寻找是否有该属性
        如果没有则会去当前对写的类中去寻找，如果没有则报错
    -类对象和实例对象中都可以保存属性(方法)
        如果这个属性(方法)是所有的实例共享的，则应该保存到类对象中
        如果这个属性(方法)是某个实例独有的，则应该保存到实例对象中
    -一般看下属性保存到实例对象中，方法保存到类对象中

'''
# p1.talk()
# p2.talk()

'''
目前name属性对于Person类对象来说是必须的，目前在创建对象后
都需要手动为对象手动添加name属性，这种方式很容易出现麻烦，
使用公共属性的方式会导致，大量用户都是同一个name。
我们希望在创建对象时，必须设置name属性，如果不设置对象将无法创建
并且属性的创建应该是自动完成的，而不是在创建对象以后手动完成的

    在类中可以定义一些特殊方法(魔术方法)
    特殊方法都是__方法名__的格式
    特殊方法不需要自己调用，会自动调用。

对象的创建流程
    1.创建一个变量
    2.在内存中创建一个新对象
    3.__init__(self)方法执行
    4.将对象的id赋值给变量
'''

# class Et():
#     def __init__(self,name) -> None:
#         self.name=name
#         print('__init__执行了') 

    #在类中定义的函数称为方法
#     def talk(self):
#         print('你好世界'+f'我是{self.name}')

# e1=Et('czz')
# e2=Et('cxc')
# e1.talk()
# e2.talk()

#目前我们可以直接通过对象.属性的方式来改变对象属性的值，这种方式不安全
# e1.name='cdy'

#我们现在需要一种方式来增强数据的安全性
#封装:隐藏对象中一些不希望被外部访问到的属性或方法
'''
    1.隐藏属性名，使调度者无法随意的修改对象中的属性
    2.增加get_ , set_ 方法，很好的控制属性是否是只读的
    3.使用set_方法设置属性，可以增加数据的验证，保障数值是正确的
    4.使用get_方法读取属性，set_方法设置属性，可以在读取和修改
    属性时同时做一些其他的处理
    5.使用get_方法还可以返回一些通过对象属性计算的结果

    可以使用__属性 开头来限制属性或方法只能在类内部访问
        -实际上还是可以通过_Class__属性=xxx来修改
        -隐藏的方法也可以通过_Class__方法()来调用
        -一般情况下使用_老表示属性是私有属性(提示作用)
'''
# class Dog():
#     def __init__(self,name) -> None:
#         self.__name=name
#         print('__init__执行了') 

#     #在类中定义的函数称为方法
#     def talk(self):
#         print('你好世界'+f'我是{self.__name}')

#     def get_name(self):
#         print('==========姓名==========')
#         return self.__name
#     def set_name(self,name):
#         if len(name) <=5:
#             self.__name=name
#             print('===========修改后姓名为==========')
#             print(self.__name)
#         else:
#             print('==========姓名过长=========')
      
# d1=Dog('czz')
# d2=Dog('cxc')
# print(d1.get_name())
# d1.set_name('陈中正')
# d1.set_name('陈中正123')
# d1._Dog__name='czz'
# print(d1.get_name())

'''
@property装饰器，用来将一个get方法，转换为对象的属性
添加property装饰器以后，可以像属性一样使用get方法

@属性名.setter 装饰器，用来将set方法转换为对象的属性
添加@属性名.setter装饰器以后可以像属性一样使用set方法

使用以上的两个装饰器，可以很便捷的控制对象属性是否可读可修改
需要注意的是，如果对一个方法添加了@属性名.setter装饰器,则必须
添加@property装饰器
'''
# class Cat():
#     def __init__(self,name) -> None:
#         self._name= name
#     def call(self):
#        print('猫叫了一声')
#     @property
#     def name(self):
#         return self._name
#     @name.setter
#     def name(self,name):
#         if len(name)<=5:
#             self._name=name
#         else:
#             print('======长度不符合规定:过长======')

# c0=Cat('陈中正')
# print(c0.name)
# c0.name='123456'
# c0.name='czz'
# print(c0.name)

'''
继承
    -比如有一个旧类，是可以算平均数的。然后这时候有一个新类，
也要用到算平均数，那么这时候我们就可以使用继承的方式。
新类继承旧类，这样子新类也就有这个功能了。
语法
    -class ClassName(BaseClassName):
在定义类的时候，可以在括号里写继承的类，如果不用继承类的时候，
也会默认继承 object 类，因为在 Python 中 object 类是一切类的父类。
    -可以使用issubclass(子类，父类)检查一个类是否是另一个的父类
上面的是单继承，Python 也是支持多继承的，具体的语法如下：
    -class ClassName(Base1,Base2,Base3):
    -多继承有一点需要注意的：若是父类中有相同的方法名，而在子类使用时
    未指定，python 在圆括号中父类的顺序，从左至右搜索 ， 即方法在子类
    中未找到时，从左到右查找父类中是否包含方法。
继承的子类的好处：
    -会继承父类的属性和方法
    -可以自己定义，覆盖父类的属性和方法
'''

'''
如果子类中有和父类中同名的方法，则会覆盖父类的方法
父类中的所有方法都会被子类继承，包括魔术方法。
子类也可以重写魔术方法
'''
# print(issubclass(Cat,object))

# class LogicCat(Cat):
#     def __init__(self,name,age) -> None:
#         '''
#     在子类的__init__中直接调用父类中的魔术方法,可以减少在
#     子类初始化过程中的冗余代码
#     由于调用魔术方法是通过类的方式调用的，所以注意传递self参数
#      Cat.__init__(self,name)
#     上面的写法会固定父类，可以直接使用super()指代父类,且使用super()
#     方法时，无需传递self参数
#         '''
#         super().__init__(name)
#         self._age=age
    
#     def call(self):
#        print(self._name+':叫了一声',sep='')
#     @property
#     def age(self):
#         return self._age
#     @age.setter
#     def age(self,age):
#         if age<20:
#             self._age=age
#         else:
#             print('======年龄不符合规定:年龄过大======')


# lc0=LogicCat('L1',18)
# print(lc0.name)
# lc0.name='mycatisbest'
# lc0.call()
# lc0.age=100
# print(lc0.age)
'''
多态
对于tell这个函数来说，只要对象中含有name属性，它就可以作为参数
传递，这个函数不会考虑对象的类型，只要有name属性即可

假如在tell()中添加了一个类型检查，则这个函数就违反了多态
'''

# class A():
#     def __init__(self,name) -> None:
#         self.name=name
# class B():
#     def __init__(self,name) -> None:
#         self.name=name
# def tell(obj):
#     print(obj.name+'说:你好')
# a0=A('czz')
# b0=B('cdy')
# tell(a0)
# tell(b0)


'''
len()
之所以一个对象能通过len()来获取长度，是因为对象中具有一个特殊方法
__len__，也就是说对象中具有__len__特殊方法，就可以通过len()来获取
长度
'''
# class Test():
#     def __len__(self):
#         return 10

# t0=Test()
# print(len(t0))

'''
面向对象的三大特征
    -封装:确保数据的读取和修改安全
    -继承:保证对象的可扩展性
    -多态:提高程序的灵活性
'''


'''
实例属性
    -通过实例对象添加的属性属于实例属性
    实例属性只能通过实例对象来访问和修改，类对象无法访问和修改
实例方法
    -在类中定义，以self为第一个参数的方法都是实例方法
    实例方法在调用时，python会传入调用对象作为self传入
    -实例方法可以通过实例和类去调用
        当通过实例调用类时，会自动传入调用对象作为self传入
        当通过类调用时，不会自动传递self，必须手动传递
类方法
    -在类内部使用@classmethod修饰的方法属于类方法
    -类方法的的第一个参数是cls，也会被自动传递
    -类方法可以被类调用，也可以被实例调用,没有区别
    -使用类调用时，cls就是调用的那个类，使用实例调用，cls就是实例的类
静态方法
    -在类中使用@staticmethod修饰的方法
    -静态方法不需要指定任何默认参数
    -静态方法可以通过类或实例去调用
    -静态方法基本上和当前类无关的方法，只是保存到当前类的函数
    -静态方法一般是工具方法，与当前类无法
'''
# class  Test0():
#     name='czz'
#     @classmethod
#     def test(cls):
#         print(cls.name)


# t0=Test0()
# t0.test()

'''
魔术方法
魔术方法一般不需要我们手动调用，
需要在一些特殊情况下自动执行

__new__ 创建对象

__init__实例化对象

__del__删除对象(当一个对象没有被引用时，python就会自动回收，
此时就会调用__del__魔术方法，或者程序运行结束时也会调用__del__
魔术方法)
'''
class Person():
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
#__str__:这个特殊方法会在尝试将对象转换为字符串时调用，它的作用可以用来转换对象转换为字符串时的结果
    def __str__(self) -> str:
        return '''
        class Person():
            def __init__(self,name,age) -> None:
            self.name=name
            self.age=age
        '''
    def __repr__(self) -> str:
        return '''
        class Person():
            def __init__(self,name,age) -> None:
                self.name=name
                self.age=age
            def __str__(self) -> str:
                return
        '''
p0=Person('czz',18)
p1=Person('cxc',20)

'''
当我们打印一个对象时，实际上打印的是__str__特殊方法的返回值
print(p0)
<__main__.Person object at 0x000001ADC5297590>
'''
print(p0)

'''
__repr__和__str__类似这个特殊方法会在当前对象使用repr()函数时调用
它的作用是指定对象在‘交互式命令行’中直接输出变量的效果。
'''

'''
其他魔术方法
__gt__:会在对象做大于比较的时候调用，该方法的返回值会作为比较结果
它需要两个参数，一个self表示当前对象，other表示和当前对象比较的对象
__lt__:小于
__le__:小于等于
__eq__:等于
__ne__:不等于
__ge__:大于等于
'''

class A():
    def __init__(self,age) -> None:
        self.age=age
    def __gt__(self,other):
        return self.age>other.age
    #__bool__将对象转换为布尔值的返回结果
    def __bool__(self):
        return self.age>=18
        
a0=A(19)
a1=A(20)
if a0:
    print('成年了')
print(a0 > a1)

