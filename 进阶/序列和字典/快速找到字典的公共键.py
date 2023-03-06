from random import randint,sample
'''
sample()从序列中随机挑选k个元素，并使用列表返回，k可以随机
print(sample(['ssad','sAS','dasda','s'],randint(1,4)))
'''

dic0={'player:%s'%k:randint(10,20) for k in sample('abcdef',randint(3,6))}
dic1={'player:%s'%k:randint(10,20) for k in sample('abcdef',randint(3,6))}
dic2={'player:%s'%k:randint(10,20) for k in sample('abcdef',randint(3,6))}
lis0=[dic0,dic1,dic2]
'''
all()如果 bool（x） 对于可迭代对象中的所有值 x 都为 True，则返回 True。
如果可迭代对象为空，则返回 True。
print(all([1,1,1])) = True
print(all([1,1,0])) = False
'''
print([k for k in lis0[0] if all (map(lambda d: k in d,lis0[1:]))])

'''
方案二:利用集合set的交集操作
'''
#取两个集合的公共key
s1=dic1.keys()
s2=dic2.keys()
#字典的key具有唯一性，所以可以使用集合操作
print(s1 & s2)
#取多个集合的公共key
'''
reduce()
print(reduce(lambda a,b:a*b,range(1,10))) = 362880
1> 1*2
2> 2*3
3> 6*4
....
'''
from functools import reduce
key_lis=[dic0.keys(),dic1.keys(),dic2.keys()]
print(reduce(lambda key_dic0,key_dic1:key_dic0 & key_dic1,key_lis ))
#上面的写法还可以简化
print(reduce(lambda key_dic0,key_dic1:key_dic0 & key_dic1 ,list(map(dict.keys,lis0))))

