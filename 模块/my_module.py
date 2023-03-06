#print('我是test_moudle')
'''
在模块中定义的变量，在引入模块后就可以直接使用了
'''
a=10
b=20
#添加了_的变量只能在模块内部被访问，在通过 from 模块名  import * 引入时就不会被引入
_c='version:12'
'''
在模块中定义的函数，在引入后也可以直接使用
'''
def fun0():
    print('this is fun0')

'''
在模块中定义的类，在引入后也可以直接使用
'''
class Person():
    def __init__(self,name) -> None:
        self._name=name

#检查当前模块是否时主模块
if __name__ == '__main__':
    print('是主模块')