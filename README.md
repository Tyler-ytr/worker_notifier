# worker_notifier
##  程序功能
1. 根据shedule.txt里面的配置按时触发windows提醒;

## 环境配置

1. `pip install -r requirements.txt`
2. 运行`generate_bat.py`生成test.bat
3. 需要保证cmd默认的python能够正确使用win_shedule.py 

## 功能配置
1. shedule.txt用于固定时间的通知;格式如下:
    ````
    09:30 干活
    23:59 睡觉
    ````
    需要注意要有四位数字否则shedule会报错;
   
##  开机自启配置

1. 搜索栏打开运行
2. 输入`shell:startup`
3. 把test.bat的快捷方式复制进去即可

PS: 需要保证`test.bat`脚本能正常运作；可以在bat末尾加上Pause来调试是否能够正确启动；