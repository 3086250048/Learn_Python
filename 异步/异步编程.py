'''概念一
    事件循环
    任务列表=[任务1，任务2,...]

    while True:
        可执行的任务列表,已完成的任务列表=去任务列表中检查所有的任,将‘可执行’和‘已完成’的任务返回

        for 就绪任务 in 已准备就绪的任务列表:
            执行已就绪的任务
        for 已完成的任务 in 已完成的任务列表:
            在任务列表中移除已经完成的任务
        如果 任务列表中的任务已经完成，则终止循环
 
'''
import asyncio
#生成一个事件循环
# loop=asyncio.get_event_loop()
#将任务放到任务列表
# loop.run_until_complete(任务)

#快速上手
'''
携程函数:定义函数的时候 加 async 的函数
携程对象:执行协程函数()得到的协程对象
'''
#定义一个携程函数
async def fun0():
    print('started')
#得到一个协程对象
result=fun0()

#python 3.7之后
asyncio.run(result)

#旧写法
# #得到一个事件循环
# loop=asyncio.get_event_loop()
# #将事件放入循环
# loop.run_until_complete(result)


