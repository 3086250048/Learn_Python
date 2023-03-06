'''
将函数作为返回值返回，也是一种高阶函数
这种高阶函数也称为闭包
形成闭包的要件
    -函数嵌套
    -将内部函数作为返回值返回
    -内部函数必须要使用到外部函数的变量
'''
global_num=0
def add(a):
    def inner_add(b):
        #如果想在内部函数使用全局的变量，却不影响全局变量。
        # 则可以在内部函数使用nonlocal关键字
        nonlocal a
        a+=b
        return a
    return inner_add
'''
f是调用add后返回的函数，这个函数是在add函数内部定义的，并不是全局函数
所以这个函数总是能访问到fn函数内的变量
可以将一些私有数据藏到闭包中
'''
f=add(global_num)
f(10)
f(20)
print(f(30))
print(global_num)

