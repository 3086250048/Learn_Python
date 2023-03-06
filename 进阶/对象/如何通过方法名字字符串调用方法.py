class Person():
    def __init__(self) -> None:
        self.method_name=['talk','tell','run','sleep']
    def UsePersonFun(self,str,*args):
        if str in self.method_name:
            f=getattr(self,str,None)
            f(*args)
        else:
            print('类中没有改方法')
    def talk(slef,str):
        print(str.center(100,'*'))
    def tell(self,name,age):
        print(f'我的名字叫{name},今年{age}岁')

p=Person()
# 方法1 getattr(obj,attribute/function,deault) ，如果对象不具有引用的属性，则会使用default的值

p.UsePersonFun('talk','你好我的名字叫陈中正')
p.UsePersonFun('tell','陈中正','18')

#技巧:如何判断一个对象中是否有某个属性或方法
print(hasattr(p,'tell'))

#方法2 使用operator.methodcaller方法
from operator import methodcaller
def talk(str):
    print(str.center(100,'*'))
#（实例化的对象可以进行调用）后加实例化的对象可以进行调用
methodcaller('UsePersonFun','tell','陈中正','18')(p)



