# python实用小技巧整理
## 指定网站下载安装包
```
pip install -i http://pypi.douban.com/simple --trusted-host pypi.douban.com pymysql
```
## 添加以下两句用于正常显示中文汉字
```
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
```
## 闭包的概念
> 函数+环境变量
，a 不能是全局变量，否则不能形成闭包。保存函数相关的现场。函数定义是外部的变量，但又不能是全局变量。
```
def curve_pre():
    a = 25
    def curve(x):
        return a*X*X
    return curve
a =10 
f = curve_pre()
f(2)
```

## python时间处理

```
str ----> date
import datetime

detester = ‘2017-01-01'
date = datetime.datetime.strptime(detester,’%Y-%m-%d')
```
```
date -----> str
import datetime

date = datetime.now()

detester = date.strftime(‘%Y-%m-%d')
```
```
# 毫秒处理
datetime.datetime.strptime(data['firstfault'][i],'%Y-%m-%d %H:%M:%S.%f')
```
```
# 向前减去30分钟
datetime.datetime.strptime(data['firstfault'][i],'%Y-%m-%d %H:%M:%S.%f')+datetime.timedelta(minutes=-30)
```
## 装饰器

我们可以接受函数定义时的复杂，不能接受函数调用时的复杂。装饰器魔法糖，便于函数调用又不破换原函数的结构，增强函数的复用性和稳定性。 https://www.jianshu.com/p/1e2394733e77
