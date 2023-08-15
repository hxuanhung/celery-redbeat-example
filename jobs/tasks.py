from datetime import datetime

from celery import schedules
from redbeat import RedBeatSchedulerEntry

from jobs.worker import celery_app


@celery_app.task
def heartBeat():
    print("-------- inside heartbeat")
    return datetime.now()


@celery_app.task
def dummy_task(name=None):
    if name:
        return {"result": f"OK {name}"}
    return False


def dummy_scheduled_task():
    # minute="15", hour="13", day_of_week="tuesday"
    crontab_interval = schedules.crontab()
    # interval = schedules.schedule(run_every=60)  # seconds
    entry = RedBeatSchedulerEntry(
        name="task-name",
        task="jobs.tasks.dummy_task",
        schedule=crontab_interval,
        args=["test"],
        app=celery_app,  # !important
    )
    entry.save()


def delete_task(key):
    """Delete a task by its key in Redis
    Key = prefix + <task name>

    Example:
    task's name is "check_heartbeat_every_5_second"
    key = redbeatcheck_heartbeat_every_5_second

    Note: there is no space in between prefix and name.
    """
    entry = RedBeatSchedulerEntry.from_key(key, app=celery_app)
    entry.delete()
