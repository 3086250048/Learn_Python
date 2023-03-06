'''
线程之间的事件通知
使用标准库中的Threading.Event

'''

from threading import Thread,Event
# def fun(event,index):
#     print(f'wait event....{index}')
#     event.wait()
#     print(f'fun end.....{index}')
# e=Event()
# t=Thread(target=fun,args=(e,'1'))
# t.start()
# #调用e.set()通知一个事件给t，使t继续执行
# e.set()
# # 调用过e.set()之后就阻塞不住了，需要调用e.clear(),清空事件
# t=Thread(target=fun,args=(e,'2'))
# t.start()
# e.clear()


'''
案例:如何在线程间进行事件通知
'''
import time
class AThread(Thread):
    def __init__(self,a_event,b_event):
        super().__init__()
        self.a_event=a_event
        self.b_event=b_event
    def run(self):
        flag=False
        while True:
            #模拟a线程第一次处理
            if not flag:
                for i in range(10000):
                    if i == 9999:
                        flag=True
                        self.b_event.set()
                
            #等待B线程转换完成,或第一次A线程运行完成
            self.b_event.wait()
            self.b_event.clear()
            #主处理过程
            for _ in range(10000):
                print('A线程处理中~~~~~~')
            print('A线程处理完成-------------------------------------------------------------------')
            time.sleep(2)
            flag0=False
            #通知b线程处理完成
            if not flag0:
                self.a_event.set()
                flag0=not flag0

class BThread(Thread):
    def __init__(self,a_event,b_event):
        super().__init__()
        self.a_event=a_event
        self.b_event=b_event
    def run(self):
        while True:
            #等待A线程处理完成
            self.a_event.wait()
            self.a_event.clear()
            #处理过程
            for _ in range(10000):
                print('B线程处理中~~~~~~~~~')
            flag=False
            print('B线程处理完成----------------------------------------------------------------')
            time.sleep(2)
            #通知a线程处理完成
            if not flag:
                self.b_event.set()
                flag= not flag
a_e=Event()
b_e=Event()

a=AThread(a_e,b_e)
b=BThread(a_e,b_e)

a.start()
b.start()
