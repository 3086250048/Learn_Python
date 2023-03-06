'''
with语句的工作流程

with open('demo.txt','w') as f:
以上语句等同于下面
'''
# F=open('demo.txt','w')
#进入with语句块，所执行的操作
# f=F.__enter__()
# print(f is F)
#退出with语句块所执行的操作
# F.__exit__()

from os import getcwd,chdir
from sys import stdin,stdout
import getpass
import telnetlib
from collections import deque

print(getcwd())
chdir(r'C:\Users\30862\Desktop\Python\进阶\对象')
class PrintA():
    def __init__(self,content) -> None:
        self.content=content
    def __enter__(self):
        print('start'.center(50,"*"))
        return self
    def __exit__(self,exc_type,exc_value,exc_tb):
        '''
            如果是正常退出with语句则这三个自动传入的
            参数都为none,如果with语句执行时没有try
            则异常会传递给这三个参数,然后再传递给下一层，
            可以通过return True 来阻止异常继续向外层抛。
            exc_type:异常类、exc_value:异常值、exc_tb:异常
            对象的地址
        '''
        print(exc_type,exc_value,exc_tb)
        print('end'.center(50,"*"))
        return True
    def out(self):
        print(self.content)

'''
以下语句的运行过程
P=PrintA('你好陈中正')
p=P.__enter__() //先打印****Start*****,然后返回self给p
p.out() //打印语句
P.__exit__() //打印*****end******
'''
with PrintA('你好陈中正') as p:
        raise Exception('异常')
        p.out()

