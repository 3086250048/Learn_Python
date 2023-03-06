'''
能放在 for in 之后的必须是一个可迭代对象
'''
from collections.abc import Iterable,Iterator
#检查一个类是否注册到了Iterable 或实现了__iter__()函数
arr=[1,2,3]
print(isinstance(arr,Iterable))
#for 循环工作流程
#1.调用 可迭代对象arr 的__iter__()函数，得到一个迭代器对象iter_obj，迭代器之间互相独立
iter_obj0=arr.__iter__()
iter_obj1=arr.__iter__()
#2.调用迭代器对象iter_obj的__next__函数
print('iter_obj0:',iter_obj0.__next__())
print('iter_obj1:',iter_obj1.__next__())
print('iter_obj0:',iter_obj0.__next__())
print('iter_obj1:',iter_obj1.__next__())
print('iter_obj0:',iter_obj0.__next__())
print('iter_obj1:',iter_obj1.__next__())
#3.迭代到抛出StopIteration异常之后结束
# print('iter_obj0:',iter_obj0.__next__())

'''
可迭代对象:iterable
迭代器对象:iterator
'''
from random import randint
dic={'day%d'%k:'今天气温%d'%randint(10,30) for k in range(20) }
print(dic)

class TemperatureIterator(Iterator):
    def __init__(self,day_lis):
        self.day_lis=day_lis
        self.index=0
    def __next__(self):
        if self.index == len(self.day_lis):
            raise StopIteration
        day_info=self.day_lis[self.index]
        self.index+=1
        return self.get_weather(day_info)
    def get_weather(self,day_info):
        return f'第{day_info}天:'+dic['day'+str(day_info)]

class TemperatureIterable(Iterable):
    def __init__(self,day_lis):
        self.day_lis=day_lis
    def __iter__(self):
        return TemperatureIterator(self.day_lis)


a=TemperatureIterable([x for x in range(1,20) if x %2==0])
b=TemperatureIterable([x for x in range(1,20) if x%2 !=0])
a1=a.__iter__()
b1=b.__iter__()
print(next(b1))
print(next(a1))
print(next(b1))
print(next(a1))
print(next(b1))
print(next(a1))
print(next(b1))
print(next(a1))
print(next(b1))
print(next(a1))
print(next(b1))
print(next(a1))