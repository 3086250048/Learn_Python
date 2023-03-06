class Player1():
    def __init__(self,uid,name,level):
        self.uid=uid
        self.name=name
        self.level=level
'''
Player2比Player1所消耗的资源更小        
'''
class Player2():
    __slots__=['uid','name','level']
    def __init__(self,uid,name,level):
        self.uid=uid
        self.name=name
        self.level=level
p1=Player1('0001','jim',10)
p2=Player2('0001','jim',10)
# print(dir(p1))
# print(dir(p2))
#可以看到p1比p2多出了两个属性，主要的内存浪费就是__dict__
print(set(dir(p1))-set(dir(p2)))
# p1.x=100
# p1.y=200
#动态添加的属性通过__dict__进行维护
print(p1.__dict__)
#也可以通过__dict__动态添加属性
# p1.__dict__['z']=200
# print(p1.__dict__)
#删除属性
# p1.__dict__.pop('x')
# print(p1.__dict__)
#可以通过sys.getsizeof查看内置类型的实例消耗大小
import sys
#可以看到动态添加属性所维护的字典的内存大小远大于
#数据本身的大小
# print(sys.getsizeof(p1.__dict__))
# print(sys.getsizeof(p1.name))
# print(sys.getsizeof(p1.uid))
# print(sys.getsizeof(p1.level))
# help(sys.getsizeof)

#通过__slots__来关闭动态添加属性，使只能操作指导的属性。
# p2.x=100

#通过tracemalloc 来动态跟踪内存使用情况
#创建一百万个实例，对比内存使用情况
import tracemalloc
tracemalloc.start()
#start
p1_=[Player1(1,1,1) for _ in range(1000000)]
p2_=[Player2(1,1,1) for _ in range(1000000)]
#end
snapshot=tracemalloc.take_snapshot()
top_stats=snapshot.statistics('lineno')
for stat in top_stats[:10]:print(stat)


