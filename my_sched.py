import schedule
import time
from run import RunMe

runMe = RunMe() 
def job():
    runMe.run()
    print("I'm working to capture...")

schedule.every(5).seconds.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:n30").do(job)
# schedule.every(5).to(10).days.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

