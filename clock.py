from apscheduler.schedulers.blocking import BlockingScheduler
from app import postTweet

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')
    postTweet()

sched.start()
