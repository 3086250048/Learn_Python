'''
语句1 if 条件表达式 else 语句2
如果条件成立执行语句1，否则执行语句2
'''

print('你好') if True else print('世界')
print('你好') if False else print('世界')
'''
获取a和b之间的较大值
'''
a=5
b=20
max=a if a>b else b
print(max)

'''
获取三个值中的最大值
'''
#写法1(不推荐)
a=20000
b=100
c=1000
max=(a if a>c else c) if a>b else (b if b>c else c)
print(max) 
#写法2
max=a if a>b else b
max= max if max>c else c
print(max)
#写法3(a<b<c == b > a and b < c )
max=c if a<b<c else (b if b>a  else a)
print(max)