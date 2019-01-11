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
