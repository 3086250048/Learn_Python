'''
函数式编程
在python中，函数是一等对象
一等对象有如下的特点
    -对象实在运行时创建的
    -能赋值给变量或作为数据结构中的元素
    -能作为参数传递
    -能作为返回值返回
高阶函数，至少要符合以下两个特点中的一个
    -接收一个或多个函数作为参数
    -将函数作为返回值返回
'''

def number_if(fun,*num):
    result=[]
    for i in num:
        if fun(i):
            result+=[i]
    return result

def eq_num(num):
    if num % 2==0:return True
    return False


print(
    number_if(eq_num,100)
)