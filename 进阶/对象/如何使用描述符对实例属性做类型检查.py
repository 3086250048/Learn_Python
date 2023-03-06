class A:
    pass
a=A()
# a.x=value
# a.__dict__['x'] = 'value'

class Attr():
    def __init__(self,key,type) -> None:
        self.key=key
        self.type=type
    def __set__(self,instance,value):
        if not isinstance(value,self.type):
            raise TypeError(f'只能接收类型为{self.type}的数据')
        instance.__dict__[self.key]=value
    def __get__(self,instance,cls):
        return instance.__dict__[self.key]
    def __delete__(self,instance):
        del instance.__dict__[self.key]

class B():
    name=Attr('name',str)
    age=Attr('age',int)

b=B()
b.name='12'
print(b.name)
b.name=12
print(b.name)