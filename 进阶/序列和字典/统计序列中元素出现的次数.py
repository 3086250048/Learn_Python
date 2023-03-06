'''
统计序列中元素出现的次数,删除出现次数前三的数和出现的次数

'''
#方案1:将序列转换为字典{元素:频率}，根据字典中的value进行排序
from random import randint
arr0=[randint(0,30) for _ in range(101)]
#创建一个value都为0的字典
dic0=dict.fromkeys(arr0,0)
for v in arr0:
    if v in dic0.keys():
        dic0[v] +=1
#写法1
# lis0=sorted(dic0.items(),key=lambda item:item[1],reverse=True)[:3]
#写法2,用() (生成器) 代替 [] (列表) 更节省性能
# lis0=sorted(((v,k) for (k,v) in dic0.items()),reverse=True)[:3]
# print(lis0)
#写法3:使用堆，最推荐
import heapq
#取元组中排序结果最大的前三个
#((v,k) for (k,v) in dic0.items()) 返回的是<generator object <genexpr> at 0x000001B54EB326C0>
# print(heapq.nlargest(3,((v,k) for (k,v) in dic0.items())))
#取元组中排序结果最小的三个
# print(heapq.nsmallest(3,((v,k) for (k,v) in dic0.items())))


#方案2:使用标准库collections中的Counter对象(最方便)
from collections import Counter
arr1=[randint(0,30) for _ in range(101)]
#根据列表中元素出现的次数自动降序排序(对字典会根据value进行排序)
counter_obj=Counter(arr1)
#取出现排序结果前三的元素
print(counter_obj.most_common(3))

#案例:统计文章中，单词出现的次数
from re import split
with open('进阶/demo.txt','r',encoding='utf-8') as file_obj:
    text=file_obj.read()
    word_lis=split('\W+',text)

counter_obj=Counter(word_lis)
print(counter_obj.most_common(3))

