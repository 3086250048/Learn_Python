class A():
    def __del__(self):
        print('in  __del__')

#只有当对象的引用为0时对象才会被回收
a=A()
a2 = a
a2 = None
a=1