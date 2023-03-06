from random import sample
from time import time
arr0=[x for x in sample('abcd'*100000,400000) ]
st=time()
str=''
for i in arr0:
    str+=i
print(time()-st)
'''
以上方法消耗内存且速度慢，可以使用str.join()方法，快速的拼接列表中的字符串
    语法: 字符串.join(可迭代对象)
'''
st=time()
str=''.join(arr0)
print(time()-st)


