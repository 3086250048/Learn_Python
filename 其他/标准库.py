'''
python标准库
sys模块，它里面提供了一些变量和函数，使我们可以获取到python解析器的信息
或通过函数来操作python解析器
'''
import sys
#<module 'sys' (built-in)> built-in 表示内置无需下载或定义
print(sys)

#获取交互式命令行的参数
print(sys.argv)
'''
输入:C:/Users/30862/AppData/Local/Programs/Python/Python311/python.exe c:/Users/30862/Desktop/Python/标准库.py aa bb cc
输出:['c:/Users/30862/Desktop/Python/标准库.py', 'aa', 'bb', 'cc']
'''

#sys.modules 获取程序中引入的所以模块
#返回一个字典，字典的key使模块的名字，字典的value使模块的存储位置
print(sys.modules)

#pprint 模块它给我们提供了一个pprint() 该方法可以对打印的数据做简单的格式化
from pprint import pprint
pprint(sys.modules)


#sys.path 返回的是一个列表，列表中保存的是模块的搜索路径
pprint(sys.path)

#sys.platform 表示python运行的平台
pprint(sys.platform)

#sys.exit() 退出程序
# sys.exit('程序异常')
# print('你好')

'''
os 模块 让我们可以对操作系统进行访问
'''
import os
print(os)

#os.environ通过这个属性可以获取系统的环境变量
pprint(os.environ['path'])

#os.system()可以用来执行操作系统的命令
for i in range(10):
    os.system('notepad')