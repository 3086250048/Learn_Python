'''
filter()函数
    -可以从序列中过滤出符合条件的元素，保存到一个新的序列中
    参数
        -函数
        -需要过滤的序列
    返回值:过滤后的新序列
'''
def eq_num(num):
    if num % 2==0:return True
    return False
'''
eq_num函数是作为参数传递进filter()函数中
eq_num函数实际上只有一个作用，就是作为filter()的参数
filter()调用完毕以后eq_num就已经没用
'''
# print(list(filter(eq_num,[1,2,3,4])))

'''
lambda函数表达式专门用来创建一些简单的函数
语法:lamdba 参数列表:返回值
'''
print(lambda a,b : a+b)
#调用
print((lambda a,b:a+b)(10,20))
#简写过滤偶数的函数
print(list(filter(lambda num:num%2==0,[1,2,3,4,101,102])))

'''
map()函数可以对可以遍历对象中的元素做指定的操作，然后将其添加到一个新的对象中返回
'''
#对数组中的偶数都加1,奇数都置为false
arr0=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda num:num%2==0 and num+1,arr0)))

'''
sort()方法默认直接比较列表中元素的大小
sort()方法可以接受一个关键字参数,key
key需要一个函数作为参数，当设置了函数作为参数
每次都会以列表中的一个元素作为函数的参数，并且使用函数的返回值比较元素的大小
'''
#按照字符串的长度排序
arr1=['a','123','adasda','2','sda','3']
arr1.sort(key=lambda str:len(str)) #等同于 arr1.sort(key=len)
print(arr1)
#比较str和int类型的数字
arr2=[1,'2',3,4]
arr2.sort(key=int)
print(arr2)

'''
sorted()
这个函数和sort()的用法基本一致，但是sorted可以对任意的序列进行排序
并且使用sorted排序，不会影响原来的对象，会返回一个新的对象
语法 sorted(序列,key=函数或lamdba)
'''
arr2='12212191889812712131321231'
print(sorted(arr2,key=int))
print(arr2)
