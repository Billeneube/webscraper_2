from apscheduler.schedulers.blocking import BlockingScheduler
import webscraper_2
sendMessage=False
debug=False


def some_job():
    webscraper_2
    print('ran')

scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', seconds=30)
scheduler.start()