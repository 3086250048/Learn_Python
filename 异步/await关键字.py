import asyncio

#await + 可等待的对象(协程对象、Future、Task对象)
# async def fun0():
#     print('started')
#     result= await asyncio.sleep(2)
#     print('finished',result)

# asyncio.run(fun0())



async def say_hello(word,delay):
    print('started')
    await asyncio.sleep(delay)
    return word

#await就是等待对象的值，得到结果之后再继续走下去
async def main():
    print('main')
    result1= await say_hello('你好',2)
    print(result1)
    result2= await say_hello('我叫czz',2)
    print(result2)

asyncio.run(main())


    