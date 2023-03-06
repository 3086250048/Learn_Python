'''
模块
将一个完整的程序分解为一个个的小的模块
通过将模块的组合来搭建一个完整的程序
模块化的优点
    -方便开发，方便维护
    -模块可以复用
在python中一个py文件就是一个模块
模块名要符合标识符规范
在一个模块中引入外部模块
    1.import 模块名(不需要跟.py，可以引入同一个模块多次，但模块的实例只会创建一次)
    2.import 模块名 as 别名
    3.import可以在程序的任意位置调用，一般情况下import语句会写在文件开头
    4.在每一个模块中都有一个__name__属性，通过这个属性可以获取模块的名字
'''
import my_module as my
#<module 'my_module' from 'c:\\Users\\30862\\Desktop\\Python\\模块\\my_module.py'>
print(my)
#my_module
print(my.__name__)
'''
__name__属性值为__main__的模块就是主模块，一个程序中只会有一个主模块
主模块就是直接通过python执行的模块(直接执行谁，谁就是主模块)
'''
#__main__
print(__name__)

#访问模块中的变量:模块名.变量
print(my.a)
print(my.b)

#访问模块中的函数:模块名.函数
my.fun0()

#访问模块中的类:模块名.类
p0=my.Person('czz')
print(p0)#<my_module.Person object at 0x0000026FF26BF750>

'''
也可以引入模块中的部分内容
语法: from 模块 import 变量,函数,类...
from 模块 import * 引入所有内容，一般不使用
也可以为引入的变量使用别名
语法: from 模块 import 变量 as new_变量,函数 as new_函数,类 as new类...
'''
from my_module import Person as P,fun0 as fun1,a as aa,b as bb
from my_module import *
print(aa)
print(bb)
fun1()
p1=P('陈中正')
print(p1)
#使用_命名的变量，不会被from 模块 import *的方式被引入
# print(_c)

'''
__pycache__是模块的缓存文件，py代码在执行之前，需要被解析器先转换为机器码，任何再执行
所以再使用模块(包)的时候，也需要将模块的代码先转换为机器码保存到文件中。
'''