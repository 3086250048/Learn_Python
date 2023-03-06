'''
set 集合和列表相似，但是只能存储不可变对象
集合不是按元素插入顺序保存的
集合中不能出现重复的元素
'''

#创建集合，使用{}或set()创建集合
set0={1,2,3,4,10,3,4,5,1,1,1}
# set1={[123,200],[1,2,3]} #集合只能存储不可变对象
set1=set() #创建一个空集合
print(type(set0))
print(set0)
print(type(set1))
set2=set([1,2,3,3,44,44,55])#set可以将序列或字典转换为集合
set3=set({'name':'czz','age':'18'})#使用set将字典转换为集合时只会包含字典的key
print(set2)
print(set3)
# print(set0[0]) #集合无法通过index操作
#集合可以使用in 和 not in 检查元素是否存在于集合中
print(1 in set0)
#len()来获取集合中的元素数量
print(len(set0))
#add()向集合中添加元素,没有返回值
set0.add(30)
print(set0)
#update()将一个不可变序列或字典中的元素添加到当前集合中
set0.update('hello')
print(set0)
#pop()随机删除集合中的元素,返回被删除的元素
result=set0.pop()
print(result)
print(set0)
#remove(指定删除集合中的元素),没有返回值
set0.remove(30)
print(set0)
#clear()清空集合
# set0.clear()
# print(set0)
#copy()对集合进行浅复制
set10=set0.copy()
set0.add(100000)
print(set0)
print(set10)

#在对集合进行运算时不会影响原来的集合，只会返回结果
print({1,2,3}&{1,2,3,4,5}) #交集运算
print({1,2,3,6,7}|{1,2,3,4,5})#并集运算
print({1,2,3,6,7}-{1,2,3,4,5})#差集
print({1,2,3,4,5}^{1,2,3,4,5,6,7})#获取异或集合（即不相交的部分）
print({1,2,3,4}<={1,2,3,4,5})#检查一个集合是否是另外一个集合的子集(空集和集合本身是任何集合的子集)
#其他情况以此类推....