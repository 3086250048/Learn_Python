'''
为元组中的元素命名
'''
student=('Jim',16,'male','3232@qq.com')
teacher=(34,'Czz')

#方案1.元组拆包赋值,用常量代替数值
name,age,sex,email=range(4)
print(student[name])

#方案2.创建一个学生枚举类,这里继承IntEnum是为了可以使用的时候就变成实例化对象，且外部不可改变值。
from enum import IntEnum
class StudentEnum(IntEnum):
    name,age,sex,email=range(4)
# StudentEnum.name=1
# print(isinstance(StudentEnum.name,StudentEnum))
print(student[StudentEnum.name])

#方案3.使用标准库collections中的namedtuple()函数，创建元组子类
from collections import namedtuple
#返回一个Student元组类
Student=namedtuple('Student',['name','age','sex','email'])
#创建一个Student元组对象
s=Student('Jim',16,'male','3232@qq.com')
#此时这样就可以像访问一个自定义类的属性一样访问元组的字段
print(s.name)
