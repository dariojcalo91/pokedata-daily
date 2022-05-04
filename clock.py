from apscheduler.schedulers.blocking import BlockingScheduler
from app import postTweet

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=9)
def scheduled_job():
    print('This job will run every day at 9am.')
    postTweet()

sched.start()
