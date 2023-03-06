'''
实现一个连续浮点发生器FloatRange,根据给定的范围(start,end)和步进值step产生一些连续浮点数
，如迭代FloatRange(3.0,4.0,0.2)可产生序列
正向3.0>3.2........>4.0
反向4.0>3.8........>3.0
'''
l=[1,2,3,4,5]
str0='helloword'
#得到一个反向迭代器<list_reverseiterator object at 0x000001DEAD606BC0>
print(reversed(l))
#也可以将其他序列传入，得到反向迭代器
for x in reversed(str0):
    print(x)

from decimal import Decimal

class FloatRange():
    def __init__(self,a,b,step):
        self.a=Decimal(str(a))
        self.b=Decimal(str(b))
        self.step=Decimal(str(step))
    def __iter__(self):
        a=self.a
        while True:
            if a>self.b:break
            yield float(a)
            a+=self.step
    def __reversed__(self):
        b=self.b
        while True:
            if b<self.a:break
            yield float(b)
            b-=self.step

f=FloatRange(1.0,9.0,0.2)
for i in f:
    print(i)
print('='*100)
for j in reversed(f):
    print(j)
