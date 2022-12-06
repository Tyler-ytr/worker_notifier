from win10toast import ToastNotifier
import schedule
import time
def notifier(words:str):
    toaster=ToastNotifier()
    toaster.show_toast("神必提醒",
                    words,
                    icon_path=None,
                    duration=5,
                    threaded=True)    
    while toaster.notification_active(): 
        time.sleep(0.1)

def everyday_notifier():
    shedule_list={}
    with open("shedule.txt","rb") as f:#shedule.txt需要UTF-8编码
        for line in f.readlines():
            temp=line.split()
            shedule_time=temp[0].decode('utf-8')
            shedule_work=temp[1].decode('utf-8') # 防止中文乱码
            shedule_list[shedule_time]=shedule_work
    for shedule_time in shedule_list:
        # print(shedule_time)
        schedule.every().day.at(shedule_time).do(notifier,shedule_list[shedule_time])

def everyhour_notifier():
    daily_list={}
    with open("daily.txt","rb") as f:
        for line in f.readlines():
            temp=line.split()
            daily_time=temp[0].decode('utf-8')
            daily_work=temp[1].decode('utf-8')
            daily_list[daily_time]=daily_work
    for daily_time in daily_list:
        # print(daily_time,daily_list[daily_time])
        # 这里的时间是分钟
        schedule.every(int(daily_time)).minutes.do(notifier,daily_list[daily_time])

def help_worker():
    notifier("启动神必提醒")
    everyhour_notifier()
    everyday_notifier()
def pending():
    while True:
       schedule.run_pending()
       time.sleep(30)

# if __name__ == '__main__':
#     everyday_notifier()

# if __name__ == '__main__':
#     notifier("开始测试")
#     # help_worker.everyday_notifier()
#     # while True:
#     #    schedule.run_pending()
#     #    time.sleep(30)