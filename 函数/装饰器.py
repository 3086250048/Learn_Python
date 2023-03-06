'''
装饰器

现在有一个需求:在开始打印前打印=======start=======
在打印结束后打印======end=======
我们可以直接通过修改函数中的代码来完成这个需求，但会产生以下问题
-如果修改的函数过多，维护起来比较麻烦
-不方便后期的维护
-违反开闭原则
    -开发对程序的扩展
    -关闭对对程序的修改
我们可以创建一个函数，自动帮助我们生产函数
我们将print_start_end函数称为装饰器
在开发中，我们都是通过装饰器来扩展函数
在定义函数时可以通过@装饰器函数名 的方式来为函数指定装饰器
可以为一个函数指定多个装饰器
'''

def print_start_end(old_fun):
    #创建一个新函数
    #在定义函数时使用*,**表示将位置参数装包为元组或将关键字参数装包为字典
    def new_fun(*args,**kwargs):
        print('='*10+'start'+'='*10)
    #在调用函数时使用*,**表示将元组或字典解包
        old_fun(*args,**kwargs)
        print('='*10+'end'+'='*10)
    #返回这个新函数
    return new_fun

#fx=print_start_end(fun)可以简写成以下的形式，直接调用就可以。
@print_start_end
def print0(str):
    print('你好',str,sep='')
@print_start_end
def print1(str):
    print('hello',str,sep='')
@print_start_end
def print3():
    print('陈中正')

# f0=print_start_end(print0)
# f1=print_start_end(print1)
# f2=print_start_end(print3)
#生产出三个地址不同的函数
# f0('世界')
# f0('word')
# f2()
print0('世界')
print1('word')
print3()
