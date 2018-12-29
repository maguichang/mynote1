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
