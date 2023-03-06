'''
字典是一种新的数据结构，称为映射(mapping)
列表的存储性能很好，但是查询数据的性能很差
在字典中每一个元素都有一个唯一的名字，在查询时，字典的效率非常快
唯一的名字称为key，对象称为value
通过key可以快速的查询value
每一对key和value称为item
'''
#字典的key可以是任意的不可变对象(tuple、str、int...),字典的value可以是任意类型对象
#字典的key不能重复，如果重复了，后声明的会覆盖
dic0={}
print(type(dic0))
#创建方式1
dic0={'name':'czz','age':'18','gender':'male'}
print(dic0)
print(dic0['name'])
#创建方式2,这种方式创建的字典key都是字符串
dic1=dict(name='czz',age=18,gender='male')
print(dic1['gender'])
#可以将包含双值子序列转换为字典
#双值子序列,序列中只有两个值 [1,2] (3,4)
#如果序列中的元素的也是序列，那么称这个元素为子序列
dic2=dict([['gender','female'],('name','czz')])
print(dic2)
#len()获取字典的item数量
print(len(dic2))
#in not in 检查字典中是否包含指定的key
print('name' in  dic2)
#通过[key]来获取值时，如果key不存在，会抛出异常keyError
#通过.get(key[,default])方式获取时，如果不存在key则会返回none
#还可以通过默认值作为参数，当key不存在时则返回定义的默认值
print(dic2.get('hello','没有这个key'))

#修改字典和添加镀锡
dic2['name']='cxc'#存在这个key则修改
print(dic2)
dic2['age']='18'#不存在这个key则添加
print(dic2)
#setdefault(key[,default]),如果字典中存在这个key则返回对于的value
#如果字典中不存在这个key，则将默认值和key添加到字典中，并返回默认值
print( dic2.setdefault('name','czz'))
print(dic2.setdefault('address','china'))
print(dic2)
#update([other])将其他字典中的item添加到当前字典中，如果有相同的key则替换调用update的字典中的item
dic3={'name':'czz','age':'18','address':'china'}
dic4={'name':'cxc','age':29}
dic3.update(dic4)
print(dic3)

#del dicx[key]删除字典中的item，删除不存在的key会报错
# del dic3['name']
print(dic3)
#popitem(),删除字典中的最后一个item,被删除的item将作为tuple返回，删除空字典也会抛出异常
print(dic3.popitem())
#pop(key[,default]),根据key删除字典中的item,会将删除的value作为返回值返回,删除不存在的key会抛出异常
#如果填写了这个default，则删除不存在的key时会返回默认值
print(dic3.pop('nam1e','没有这个key'))
#clear()清空字典，删除所有item
dic3.clear()
#copy()该方法用于对字典浅复制
#通过浅拷贝赋值的对象和原对象之间互相独立，修改一个不会影响另一个
#注意浅复制只会简单的复制对象的值，如果对象的值是一个可变对象，则依旧保留普通赋值的性状
dic4={'name':'czz','age':'18','gender':'male'}
dic5=dic4.copy()
dic4['name']='cxc'
print(id(dic4))
print(id(dic5))
print(dic4)
print(dic5)
#遍历字典
#keys()返回一个序列,values()返回一个序列,items()返回双值子序列
for key in dic4.keys():
    print(key)
for value in dic4.values():
    print(value)
for key,value in dic4.items():
    print(key,value)