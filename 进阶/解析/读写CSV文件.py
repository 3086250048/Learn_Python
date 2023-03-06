import csv
'''
csv默认用,作为分隔符，如果某个字段中包含逗号，则需要使用双引号将这个字段引起来
'''
file_obj=open('进阶/book.csv','r',encoding='utf-8')
#csv reder 需要一个已读模式打开的文件对象作为参数传入，构造一个csv reder对象
#delimiter用于指定分割符号，默认csv为逗号
csv_obj=csv.reader(file_obj,delimiter=',')
#可迭代对象可以使用__next__方法进行迭代
csv_obj.__next__
print(list(csv_obj))
# print(next(csv_obj))
# print(next(csv_obj))
# print(next(csv_obj))
#也可以使用for循环进行迭代
for info in csv_obj:
    print(info)
file_obj.close()
'''
写csv文件
'''
#同样需要一个以写模式打开的文件对象,newline=''指定写入换行只为一行
file_obj=open('进阶/write.csv','w',encoding='utf-8',newline='')
#构造csv write对象,使用delimiter 指定使用空格作为分隔符
csv_obj = csv.writer(file_obj,delimiter=' ')
#使用writerow()将一个列表全部写入csv的同一行,writerows()将一个二维列表中的每一个列表写为一行
csv_obj.writerow(['x','y','z'])
csv_obj.writerows([['1','2','3'],['4','5','6']])
#Python 文件 flush() 方法是用来把文件从内存buffer（缓冲区）中强制刷新到硬盘中，同时清空缓冲区。
file_obj.flush()
file_obj.close()

'''
案例:将出版信息大于1993年的图书信息放入new_book.csv中,使用'|'分割
'''
with open('进阶/book.csv','r',encoding='utf-8') as file_obj:
    csv_reder_obj=csv.reader(file_obj,delimiter=',')
    header_content=next(csv_reder_obj)
    with open('进阶/new_book.csv','w',encoding='utf-8',newline='') as file_obj:
      csv_write_obj=csv.writer(file_obj,delimiter='|')
      csv_write_obj.writerow(header_content)
      for info in csv_reder_obj:
         if int(info[2]) >=1993:
            csv_write_obj.writerow(info)
