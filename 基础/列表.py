'''
列表是python中的一个对象
对象object就是内存中专门用来存储数据的一块区域
之前我们学习的对象，像数值，它只能保存单一的数据
列表中可以保存多个有序的数据,列表中存储的数据称为元素
列表可以称为存储对象的对象
列表可以存储任意的对象
列表的使用
    1.列表的创建 
    2.操作列表中你的数据
'''
lis0=[]
print(type(lis0))
print(id(lis0))
lis1=[10,20]#创建一个初始值为10,20的列表
print(lis0)
lis2=[1.2,'12',None,100,[123]]#列表中存储的对象按照插入的顺序存储
print(lis2)
print(lis2[2] is None)#可以通过索引来获取列表中的指定元素，从0开始
# print(lis2[5])#IndexError: list index out of ranges索引超出后会报错
print(len(lis2))#通过len()函数获取函数的长度，长度=最大的索引+1
print(lis2[-1])#如果索引是负数，则会从后向前取，-1为倒数第一个

#列表切片_1 会包括起始位置，不会包括结束位置[i,j)
print(lis2[1:])#从开始位置截取刀最后
print(lis2[:-1])#开头截取到结束位置之前
print(id(lis2) , id(lis2[:]))#开始和结束都省略就是全部截取，相当于将列表复制了一次
#列表切片_2 [开始:结束:步长] 步长不能为0，默认是1，可以是负数(负数会从列表的后部向前面取值)
print(lis2[::2])
print(lis2[::-1])
#列表的 + *
lis3=lis2+[1,2]
print(lis3)
lis3*=3
print(lis3)
# in 和 not in
print(123 not in lis2)
print([123] in lis2)
print('a' in 'abc')
#max() 和 min()
# lis4=[1,2,3,4]
# print(min(lis4))
# print(max(lis4))

#index (获取元素在列表中第一次出现时的索引，如果列表中没有此元素则报错)和 count
#index(元素,[i,[j]]) ,i 表示查找开始的位置，j表示查找结束的元素索引之后的位置[i,j)
print(lis3)
print(lis3.index([123],5,12))

#count() 统计一个元素在列表中出现的次数
print(lis3.count([123]))

#修改列表中的元素和删除列表中的元素
print(lis2)
# lis2[0]='hello word'
# print(lis2)
# del lis2[0]
# print(lis2)

#通过切片来修改列表,通过切片来赋值时只能传递序列(str,tuple)否则报错,切片影响删除元素的范围
#并且如果设置了步长，则添加的序列中的元素要等于切片的段数否则报错
#可以利用这种方式删除元素
lis2[1::2]='ab'
print(lis2)
lis2[::]=[]
print(lis2)
lis2 += ["你好"]
print(lis2)
#列表方法 append()将括号中的元素作为整体添加到列表当中,等同于+=[x]
lis2.append("你好")
print(lis2)
#列表方法 insert()向列表中的指定位置插入一个元素
#参数:1.要插入的位置(插入位置的元素和之后的元素整体向后移动,如果超出列表的索引则默认添加到最后)
#     2.要插入的元素
lis2.insert(100,'世界')
print(lis2)
#extend()使用新的序列扩展当前的序列，等同于+=[x,xx,xxx]
#arrx.clear()清空序列等同于arrx[::]=[]
#pop()根据索引删除并返回指定元素,默认删除最后一个
# print(lis2.pop(0))
# print(lis2)
#remove()根据元素删除列表中的元素，如果相同值有多个则只会删除第一个
lis2.remove('你好')
print(lis2)
#reverse()等同于arr[::-1]
lis2.reverse()
print(lis2)
print(lis2[::-1])
#sort()对列表中的数进行排序,默认升序,在括号内填写reverse=True 设置为降序排列
str0='123asfjsfdhuiw4590'
arr=list(str0)
arr.sort(reverse=True)
print(arr) 

#遍历列表
#   for 变量 in 序列:
#       代码块
#
for value in arr:
    print(value)
