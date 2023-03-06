from threading import Thread


def printa(str0):
    print(str0.center(100,'*'))
    time.sleep(3)
import time

# t0=time.time()
# t1=Thread(target=printa,args=(('你好世界1',)))
# t2=Thread(target=printa,args=(('你好世界2',)))
# t3=Thread(target=printa,args=(('你好世界3',)))
# t1.start()
# t1.join(3)
# t2.start()
# t2.join(3)
# t3.start()

# print(time.time()-t0)
# print('main threading over')
# t0=time.time()
# for _ in range(1000):
#     printa('你好世界')
# print(time.time()-t0)
class MyThread(Thread):
    def __init__(self,str0):
        super().__init__()
        self.str0=str0
    def run(self) -> None:
        printa(self.str0)
if __name__ == '__main__':
    
    thread_list=[]
    t0=time.time()
    for i in range(1000):
        t=MyThread('你好世界%d'%i)
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()
    # 在python 线程只能对I/O操作进行加速，无法对CPU操作进行加速
    print(time.time()-t0)