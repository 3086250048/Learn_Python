import os
os.chdir(r'C:\Users\30862\Desktop\Python\文件')
with open('demo.txt','rb') as file_obj:
    '''
        seek()用于修改当前开始读取的位置,seek()需要两个参数   
            -要切换到的位置
                100就是从100字节开始读
            -计算位置的方式
                -0 从头开始计算，默认值
                -1 从当前位置开始计算
                -2 从最后位置开始计算
    ''' 
    file_obj.seek(100)
    file_obj.seek(100,1)
    print(file_obj.read(10))
    #tell()方法用来查看当前的读取的位置，返回值是字节，中文3个字节对应一个汉字。
    print(f'当前读取到了{file_obj.tell()}')
