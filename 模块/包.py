'''
包也是一个模块
当我们模块中的代码过多，需要继续细分时，就需要使用包
普通的模块就是一个py文件，而包就是一个文件夹
包中必须包含一个__init__.py这个文件，这个文件中可以包含有包中的主要内容
包文件夹下还可以添加其他相关 模块.py文件
'''
from my_package import test_module 
import my_package
print(my_package)
print(my_package.a)
print(my_package.b)
my_package.test()
test_module.test()