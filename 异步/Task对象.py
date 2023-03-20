#Task对象
#作用:帮助在事件循环中添加任务
#Task用于并发调度协程,通过asyncio.create_task(协程对象)的方式创建Task对象，这样可以让协程加入事件循环中
#等待被调度执行。除了使用asyncio.create_task()函数以外，还可以使用低层级的loop.create_task()或ensure_future()
#函数。
import asyncio
async def fun(word,delay):
    print('satrted')
    await asyncio.sleep(delay)
    return word

# async def main():

#     print('main,started')
#     #创建task对象，将当前执行func函数任务添加到事件循环
#     task1=asyncio.create_task(fun('你好',2))
#      #创建task对象，将当前执行func函数任务添加到事件循环
#     task2=asyncio.create_task(fun('世界',2))
#     print('mainfinished')

#     result1=await task1
#     result2=await task2
#     print(result1,result2)

# asyncio.run(main())

#换一种写法
async def main():

    print('main,started')
    
    task1_list=[
        #创建task对象，将当前执行func函数任务添加到事件循环，可以给Task命名
        asyncio.create_task(fun('你好',2),name='第一个'),
        asyncio.create_task(fun('世界',2),name='第二个')
    ]
    print('mainfinished')

    #如果task对象放在列表中，则需要用asyncio.wait()接受
    #done接受返回值是一个set,timeout为等待时间，如果超出等待事件则pending为没有完成的IO任务，一般情况下timeout=none
    done,pending= await asyncio.wait(task1_list,timeout=None)
    print(done)

asyncio.run(main())

