from apscheduler.schedulers.blocking import BlockingScheduler
from app import postTweet

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=5)
def scheduled_job():
    print('This job is run every 5 mins.')
    postTweet()

sched.start()
