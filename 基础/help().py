'''
help()是python中的内置函数
通过help可以查看python中的函数的用法
语法:help(函数对象)
'''
help(print)
print('你好','世界',sep='')

'''
在我们定义函数时，可以在函数内部编写文档字符串，这样就可以使用help(fun_name)来查看函数的说明
如果需要查看形参的期望传入的参数类型则可以使用  形参:str 这种方式来标明(如果有默认值则直接跟
在str只后即可),  (...) -> int 表示函数返回的数值类型为整型.
'''

def fun0(a:str,b:int,c:dict={}) -> bool : 
    '''
    你好这是一个文档字符串事例
    '''

help(fun0)
