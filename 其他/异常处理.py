'''
程序在运行过程中，不免会出现的一些错误
    -程序运行过程中，一旦出现异常就会导致程序中断

    try:
        代码块(可能出错的语句)
    except:
        代码块（出错以后的处理方式）
    else:
        代码块(没有出错的处理方式)
    
    异常的传播:
        -当在函数中出现异常时，如果在函数中对异常进行了处理则不会继续向上传播
            如果在函数中没有处理，则会传播到函数的调用处，直到传递到全局作用域
            如果依旧没有处理，则会终止程序抛出异常。
    当程序运行过程中出现异常以后，所以的异常信息都会被保存到一个专门的异常对象中，
    而异常传播时，实际上就是异常对象抛给了调用处

        异常类
            - ZeroDivisionError类的对象专门表示除数为0的异常
              NameError类的对象专门处理变量的错误
              '''
def fun0():
    print('hello')
    try:
        # print(a)
        # print(10/0)
        print(1+'121')
    except NameError:
        #如果excpet后不跟任何内容就会捕获所以类的异常
        #如果在except后跟一个异常类型，那么它只会捕获该异常
        print('打印对象没有定义')
    except ZeroDivisionError:
        print('除数为0')
     #Exception 是所有异常的父类
     #此时可以在异常类后边跟一个as xx 此时 xx就是异常对象
    except Exception as e:
        print('未知异常:',e,sep='')
    #无论是否出现异常finally都会执行
    finally:
        print('=====结束=====')
    
    #try语句是必须的，else有没有都可以，except和finally必须有一个
fun0()


'''
抛出异常
'''
#也可以自定义异常类，只需呀创建一个类继承Exception即可
class AppError(Exception):
    pass
def add(a,b):
    if a<0 or b<0:
        #raise用于向外部抛出异常，后面可以跟一个异常类或异常的实例
        # raise Exception('参数中不能有负数')
        raise AppError('参数中不能有负数')
    return a+b
add(-1,1)

