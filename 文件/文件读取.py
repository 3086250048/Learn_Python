'''
操作文件的步骤
    -打开文件
    -对文件进行各种操作(读、写),然后保存
    -关闭文件
'''

r'''
打开文件
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True,
  opener=None)
    -open()函数会返回一个对象，这个对象就是当前打开的文件
    -如果打开的目标文件和当前文件在同一级目录下，则直接写文件名即可
    -windows中使用路径时，可以使用/代替\，或者使用r'xx\xx\xx '来取消转义
    -如果目标文件距离当前文件较远，可以使用绝对路径
'''
# file_name=r'C:\Users\30862\Desktop\明日.txt'
#  file_name='demo.txt'
# file_obj  =open(file_name)
# print(file_obj)

'''
读取文件
read()方法会将内容保存为字符串返回
'''
# file_str=file_obj.read()
# print(file_str)

'''
关闭文件
close()方法会关闭文件
'''
# file_obj.close()

'''
with .... as语句
在下面的with语句中，将open(file_name) 返回值赋值给了 file_obj
在with语句中可以直接使用file_obj来操作文件,此时这个文件只能在with
中操作,写with语句结束会自动调用close()函数关闭文件.

调用open()打开文件,可以将文件分成两种类型
一种是纯文本文件(使用utf-8等编码编写的文本文件)
一种是,二进制文件(图片\mp3\ppt等这些文件)
open()打开文件默认使用文本文件形式打开,但是open()默认的编码为none
所以处理文件时,必须指定文件编码.

如果直接调用read(),会读取文件的全部内容,如果文件的内容较大,会将全部内容加载到内存中,容易导致内存泄漏
read()可以接受一个size作为参数,该参数指定读取字符数量,默认为-1表示所有字符
    可以为size指定一个值,这样read()会读取指定数量的字符
    每一次读取都是从上一次读取的位置开始读取.
    如果字符数量小于size,则会读取所有
    如果已经读取到了文件最后,则会返回''
'''

#以下是操作文件的标准格式
# file_name='demo.txt'
# # file_name=r'C:\Users\30862\Desktop\明日.txt'
# try:
#     with open(file_name,encoding='utf-8') as file_obj:
#         print(file_obj.read(10))
#         print(file_obj.read(10))
#         print(file_obj.read(10))
#         print(file_obj.read(10))
# except FileNotFoundError:
#      print('文件不存在')



'''
读取大文件时最好使用分块读取
'''
# file_name=r'C:\Users\30862\Desktop\明日.txt'
# try:
#     with open(file_name,encoding='utf-8') as file_obj:
#         result=''
#         trunk=100
#         while True:
#             content=file_obj.read(trunk)
#             if not content:break
#             result+=content
# except FileNotFoundError:
#     print('文件不存在')

# print(result)


'''
readline()可以读取一行内容
readlines()可以将读取的内容分行的装到列表中,并且可以使用[index]读取指定的行
for i in file_obj:也可以直接读取文件的每一行
'''
# from pprint import pprint
# with open('demo.txt',encoding='utf-8') as file_obj:
#     print(file_obj.readline())
#     pprint(file_obj.readlines())
    # for text in file_obj:
    #     print(text,end='')