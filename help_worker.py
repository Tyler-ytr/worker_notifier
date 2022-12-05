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
        print(shedule_time)
        schedule.every().day.at(shedule_time).do(notifier,shedule_work)



# if __name__ == '__main__':
#     everyday_notifier()

     
# toaster = ToastNotifier()

# # 有icon的版本
# toaster.show_toast("Hello World!!!",
#                    "Python is 10 seconds awsm!",
#                    icon_path="custom.ico",
#                    duration=10)

# # 无icon，采用python的icon，且采用自己的线程
# toaster.show_toast("Example two",
#                    "This notification is in it's own thread!",
#                    icon_path=None,
#                    duration=5,
#                    threaded=True)

# # 等待提示框关闭
# while toaster.notification_active(): time.sleep(0.1)