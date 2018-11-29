# Python的list，array，dict处理


## 1.dict
### 1.1
```
del dict['Name']; # 删除键是'Name'的条目
dict.clear();     # 清空词典所有条目
del dict ;        # 删除词典

遍历
for d,x in dict.items():
    print "key:"+d+",value:"+x

```
### 1.2 将列表转化为字典

```
{'key1':'1','key2':'2','key3':'3'}

>>>list1 = ['key1','key2','key3']

>>>list2 = ['1','2','3']

>>>dict(zip(list1,list2))

{'key1':'1','key2':'2','key3':'3'}
```
#### 将嵌套列表转化为字典

```
>>>new_list= [['key1','value1'],['key2','value2'],['key3','value3']]

>>>dict(list)

{'key3': 'value3', 'key2': 'value2', 'key1': 'value1'}
```
### 1.3合并嵌套字典

```
#合并嵌套字典
x={'2017-01':{'a':{'1#':1}}}
y={'2017-01':{'a':{'2#':1}}}
for k in x:
    if k in y:
        x[k]['a'].update(y[k]['a'])
```

```
合并相同键元素
dict=[{'a':"",'b':2},{'a':3,'b':4}]
from collections import defaultdict
dic={}
for _ in dict:
    for k,v in _.items():
        dic.setdefault(k,[]).append(v)
        
ll=[{k:v} for k,v in dic.items()]
print ll
print dic
print dic["a"]
a=dic["a"]
```




## 2 list
### Python实现列表对应元素求和

```
import math  
import numpy as np  
a= [1,2,3]   
b =[4,5,6]
#方法一
c=[]  
for i,j in zip(a,b):  
    summ=i+j  
    c.append(summ)  
print(c)
#方法二
c=[i+j for i,j in zip(a,b)]




```
##### 嵌套列表实现对应元素求和
先将嵌套列表转化为array，在进行多个array直接相加

```
import numpy as np
a = np.array([[1, 2],
              [3, 4],[5,6]])
b = np.array([[5, 6],
              [7, 8],[0,0]])
a+b
```

#### 嵌套列表展开


```
问题1：对于列表形如 list_1 = [[1, 2], [3, 4, 5], [6, 7], [8], [9]] 转化成列表 list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9] 的问题。
# 普通方法
list_1 = [[1, 2], [3, 4, 5], [6, 7], [8], [9]]
list_2 = []
for _ in list_1:
    list_2 += _
print(list_2)
 
# 列表推导
list_1 = [[1, 2], [3, 4, 5], [6, 7], [8], [9]]
list_2 = [i for k in list_1 for i in k]
print(list_2)
 
# 使用sum
list_1 = [[1, 2], [3, 4, 5], [6, 7], [8], [9]]
list_2 = sum(list_1, [])
print(list_2)




问题2：对于复杂一些的，如：list =[1,[2],[[3]],[[4,[5],6]],7,8,[9]]，上面的方法就不好使了。得换个方法了，这里使用递归的方法解决。
def flat(nums):
    res = []
    for i in nums:
        if isinstance(i, list):
            res.extend(flat(i))
        else:
            res.append(i)
    return res

```
#### 列表赋初值


```
标准写法：
listVal = [];
for i in range(100):
   listVal.append(0);
快速写法1：
listVal = [[0]*100];
快速写法2：
listZero = [0]
listVal = listZero * 100;

```




## 3 array


https://www.cnblogs.com/moon1992/p/4946114.html


### numpy的array和python中自带的list之间相互转化

```
a=([3.234,34,3.777,6.33])

a为python的list类型
将a转化为numpy的array:  
np.array(a)
array([  3.234,  34.   ,   3.777,   6.33 ])

将a转化为python的list
a.tolist()
```
## 4 str 与list 的相互转化


#### 4.1.str >>>list 
```

str1 = "12345"  
list1 = list(str1)  
print list1  
  
str2 = "123 sjhid dhi"  
list2 = str2.split() #or list2 = str2.split(" ")  
print list2  
  
str3 = "www.google.com"  
list3 = str3.split(".")  
print list3  
输出：
['1', '2', '3', '4', '5']  
['123', 'sjhid', 'dhi']  
['www', 'google', 'com']  

```

#### 4.2.list >>>str

```
str4 = "".join(list3)  
print str4  
str5 = ".".join(list3)  
print str5  
str6 = " ".join(list3)  
print str6  

#输出为
wwwgooglecom  
www.google.com  
www google com  
```
## 字典内列表对应数据求和
```
s=[0,0,0]
x={'a':[1,23,4],'b':[1,0,2]}
for k,v in x.items():
    s=[i+j for i,j in zip(s,x[k])]
  ```  
  
  
## 返回内容的同时返回索引,关键字enumerate
```
x=[1,2,3]
y=[4,5,6]
z=zip(x,y)

for i,j in enumerate(z):
    print i,j
```


## 字典排序（重要）

```
# 按键排序函数（前提将字典的键转换为整数）
def sortedDictValues1(adict):
    
    items = adict.items()
    items.sort()
    return [value  for key, value  in items]


x_data=sorted(d7.keys())

x_data2=[str(i)+str('#') for i in x_data]
##y_data1存储机组可利用率
y_data1=sortedDictValues1(d7)
y_data2=sortedDictValues1(d8)
y_data1_1 = [str(i)+str('%') for i in y_data1]
y_data2_1 = [str(i)+str('%') for i in y_data2]

returnData['x']=x_data2
returnData['y1']=y_data1
returnData['y2']=y_data2
```
http://blog.csdn.net/xsj_blog/article/details/51847831





# python集合
frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素

https://www.cnblogs.com/panwenbin-logs/p/5519617.html

```
s.issubset(t)  
s <= t  
测试是否 s 中的每一个元素都在 t 中  
  
s.issuperset(t)  
s >= t  
测试是否 t 中的每一个元素都在 s 中  
  
s.union(t)  
s | t  
返回一个新的 set 包含 s 和 t 中的每一个元素  
  
s.intersection(t)  
s & t  
返回一个新的 set 包含 s 和 t 中的公共元素  
  
s.difference(t)  
s - t  
返回一个新的 set 包含 s 中有但是 t 中没有的元素  
  
s.symmetric_difference(t)  
s ^ t  
返回一个新的 set 包含 s 和 t 中不重复的元素  
```

### DataFrame去重复

```
# 去除重复行数据 keep:'first':保留重复行的第一行，'last':保留重复行的最后一行,False：删除所有重复行
df = df.drop_duplicates(

　　subset=['YJML','EJML','SJML','WZLB','GGXHPZ','CGMS'], # 去重列，按这些列进行去重

　　keep='first' # 保存第一条重复数据

)
```
## python字符串处理

```
>>>s = 'hello'
>>>s[0:3]
'he' 
>>>s[:] #截取全部字符
'hello'
```
### 消除空格及特殊符号

```
s.strip() #消除字符串s左右两边的空白字符（包括'\t'，'\n','\r',''）
 
s.strip('0') #消除字符串s左右两边的特殊字符（如'0'）,字符串中间的'0'不会删除
例如：
>>>s = '000hello00world000'
>>>s.strip('0')
'hello00world'
 
s.strip('12')等价于s.strip('21')
例如：
>>>s = '12hello21'
>>>s.strip('12')
'hello'
 
lstrip,rstrip 用法与strip类似，分别用于消除左、右的字符
```
### 字符串内替换 

```
replace方法：
把字符串中的旧串替换成新串
语法为：
    str.replace(old,new[,max]) #old为旧串，new为新串，max可选，为替换次数
 
例子：
>>>s1 = 'today is a find day'
>>>s1.replace('find','rainy')
'today is a rainy day'
```
# python 判断dataframe是否为空

DataFrame有一个属性为empty，直接用DataFrame.empty判断就行。
如果df为空，则 df.empty 返回 True，反之 返回False。
注意empty后面不要加()。

```
if data.empty == False:
```
## dataframe变相实现相邻元素相减

```
data ["x1"]= data["x"].shift(1)
data["x2"] = data["x"] - data["x1"]
```
## dataframe 实现重置索引


```
import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(20).reshape(5,4),index=[1,3,4,6,8])
print(df)
我们使用reset_index()来处理：

print(df.reset_index())

可以看到此时获得了新的index列，而原来的index变成了我们的数据列，保留了下来。

如果我们不想保留原来的index，直接使用重置后的索引，那么可以使用参数drop=True，默认值是False
print(df.reset_index(drop=True))

```
