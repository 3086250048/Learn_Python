
'生成器函数'
def fun0():
    yield print('this is 1')
    yield 
    print('this is 2')
    yield
    print('this is 3')
    yield 33333
    print('this is 4')
    yield 4

from collections.abc import Iterable,Iterator
print(isinstance(fun0(),Iterator))
print(isinstance(fun0(),Iterable))
g = fun0()
next(g)
print(next(g))
print(next(g))

def fun1():
    sum=0
    while True:
        if sum % 2==0:yield print(sum)
        sum+=1

g=fun1()
for _ in range(1000):
    g.__next__()

'''
实现一个可迭代对象的类，它能迭代出给定范围内的所有素数
'''
class PrimeNumberIterable(Iterable):
    def __init__(self,a,b):
        self.a=a
        self.b=b
   
    def __iter__(self):
         for i in range(self.a,self.b+1): 
            flag=False
            if i ==1: continue
            for j in range(2,i):
                if i%j==0:flag=True
            if not flag:yield i
            
g=PrimeNumberIterable(1,30)
for i in g:
    print(i)