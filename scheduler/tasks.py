from celery import Celery
from time import sleep

app = Celery('scheduler', broker='redis://localhost')


@app.task()
def printer():
	sleep(2)
	print("Amin Saedi Celery Task Scheduler")

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('printer') every 10 seconds.
    sender.add_periodic_task(10.0, printer.s(), name='add every 10')
