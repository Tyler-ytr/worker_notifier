import help_worker
import schedule
import time

if __name__ == '__main__':
    help_worker.everyday_notifier()
    while True:
       schedule.run_pending()
       time.sleep(30)