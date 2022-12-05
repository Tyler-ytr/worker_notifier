# worker_notifier
##  程序功能
1. 根据shedule.txt里面的配置按时触发windows提醒;

##　环境配置

1. `pip install -r requirements.txt`
2. 配置test.bat`cd \worker\help_worker`为当前目录
3. 需要保证cmd默认的python能够正确使用win_shedule.py 
4. shedule.txt里的时间格式应该为"09:30"保证有4个数字;
   
##  开机自启配置

1. 搜索栏打开运行
2. 输入`shell:startup`
3. 把test.bat的快捷方式复制进去即可

PS: 需要保证脚本能正常运作；可以在bat末尾加上Pause来调试是否能够正确启动；