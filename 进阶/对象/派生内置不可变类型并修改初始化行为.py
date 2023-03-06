'''
__new__() 的目的主要是允许不可变类型的子类 (例如 int, str 或 tuple) 定制实例创建过程。
它也常会在自定义元类中被重载以便定制类创建过程。
'''
class A():
    # 1.A类这个对象被传给A类的__new__中的cls这个参数,其余参数由*args接收
    # 2.在A类的__new__中打印(1,2)
    # 3.将A类这个对象传递给object类的__new__中的cls这个参数，object的__new__会返回一个A类实例
    # 4.A类的实例被A类的__new__中的return以self的形式，返回给A类的__init__，
    #   A类的__new__中的其余参数传递给A类的__init__
    def __new__(cls,*args):
        print('In A.__new__',args)
        return object.__new__(cls)
    #1.其实只要__new__就可以将实例返回给调用者，__init__相对于一个对实例进行装饰的过程，
    #  所以__init__在装饰完实例之后会返回none
    def __init__(self,*args):
        print('In A.__init__',args)
a=A(1,2)

'''
根据上诉过程自定义元组派生类(由于元组没有实现__init__方法，所以需要直接将过程的步骤放在派生类的__new__
方法中，然后将过滤的数据连同cls传入tuple的__new__方法中，最后将其return到调用者,否则在__init__只会
拿到被转换成元组的未过滤对象,此时由于元组为不可变对象所以无法过滤。
'''

class MyTuple(tuple):
    #元组没有实现__init__方法，且初始化过程均在__new__中完成
    def __new__(cls,iterable):
        new_iter=[x for x in iterable if isinstance(x,int) and x >=0 ]
        #__new__不会和__init__一样自动返回
        return super().__new__(cls,new_iter)

mt=MyTuple([1,'2','-1',-1,2,3,4,5])
print(mt)

'''
自定义str类
'''
import re
class MyStr(str):
    def __new__(cls,str):
        new_str=re.sub('[ \r\n]+','',str)
        return super().__new__(cls,new_str)
a=MyStr('你 好我 叫 陈 \n\n\n\r\n中正')
print(a)