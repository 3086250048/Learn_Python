import os
from pprint import pprint
#os.listdir()获取指定目录的目录结构，默认路径为.表示当前目录
#该方法会返回一个列表，目录中的每一个文件的名字就是列表中的元素
#参数为 要查看的文件夹路径
dir = os.listdir('..')
pprint(dir)

#os.getcwd()
#获取当前的工作目录
print(os.getcwd())
#os.chdir()改变当前的工作目录
# os.chdir('..')
print(os.getcwd())
#os.mkdir("")默认在当前的工作目录下创建目录
os.mkdir('mkdir')
#os.rmdir("")默认删除当前工作目录下的文件夹
os.rmdir('mkdir')
#os.remove("")默认删除当前工作目录下的文件
# os.remove('path.py')
#os.rename("旧名字","新名字"),也可以不改名用来移动文件
os.rename('文件/demo1.txt','C:/Users/30862/Desktop/demo.txt')