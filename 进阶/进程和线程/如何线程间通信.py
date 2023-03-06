# 使用标准库中queue.Queue 它是一个线程安全队列
from threading import Thread
from queue import Queue
import time
class StrAddThread(Thread):
    def __init__(self,str0,queue):
        super().__init__()
        self.str0=str0
        self.queue=queue
    def run(self) -> None:
        flag=False
        while not flag:
            self.queue.put(self.print_())
            flag=True
    def print_(self):
        time.sleep(3)
        self.str0+='你好'
        return self.str0

class StrPrint(Thread):
    def __init__(self,queue):
        super().__init__()
        self.queue=queue
    def run(self):
        while True:
            print(self.queue.get())
if __name__=='__main__':
    thread_list=[]
    queue=Queue()
    for _ in range(10):
        t0=StrAddThread('陈中正',queue)
        t0.start()
        thread_list.append(t0)
    t1=StrPrint(queue)
    t1.start()  
    for t in thread_list:
        t.join()
