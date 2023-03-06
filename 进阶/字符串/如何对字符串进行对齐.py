from random import randint
dir={'name':'czz','address':'lx','manager':'Doc.Li','convertstation':'none'}
a=max(map(len,dir.keys()))
'''
方法1:使用字符串方法str.ljust(),str.rjust(),str.center()进行左右居中对齐
'''
for k,v in dir.items():
    print(k.ljust(a)+' : '+v)
  


