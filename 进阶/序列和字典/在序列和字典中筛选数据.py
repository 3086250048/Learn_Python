'''
列表
        -[x for x in arr0 if x>=0]
        -filter(lambda x:x>0,arr0) 
字典
        -{k:v for k,v in dic.items() if v > 90}
        #此时 item 是一个元组
        -filter(lambda item:item[1]>70,dir0.items())
集合
        -{x for x in set if x%3==0}
'''

from random import randint
arr0=[1,-11,2,-31,99,-100,120]
result=list(filter(lambda i:i>=0,arr0))
result=[x for x in arr0 if x >=0]
print(result)

dir0={'student%d' %i: randint(50,100) for i in range(1,21)}
new_dir0={v:k for v,k in dir0.items() if k>=70}
print(new_dir0)


set0={randint(0,20) for _ in range(0,21) }
new_set0={i for i in set0 if i %3==0}
new_set0=set(filter(lambda i:i%3==0,set0))
print(new_set0)