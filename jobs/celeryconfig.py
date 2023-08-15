"""
Configuration ->
. broker -> redis://localhost:6379/10
. loader -> celery.loaders.app.AppLoader
. scheduler -> redbeat.schedulers.RedBeatScheduler
    . redis -> redis://localhost:6379/11
    . lock -> `redbeat:lock` 25.00 seconds (25s)
. logfile -> [stderr]@%DEBUG
. maxinterval -> 5.00 seconds (5s)
"""

imports = ("jobs.tasks",)
# Here 10 is the redis's database Number
broker_url = "redis://localhost:6379/10"
# List of modules to import when the Celery worker starts.

# redbeat
redbeat_redis_url = "redis://localhost:6379/11"
redbeat_key_prefix = (
    "redbeat"  # tried with redbeat_ but the _ didn't show in Redis' key
)

result_backend = "redis://localhost:6379/10"
beat_scheduler = "redbeat.RedBeatScheduler"

# The maximum number of seconds beat can sleep between checking the schedule
beat_max_loop_interval = 5
redbeat_key_prefix = "redbeat"

# For testing purpose only
beat_schedule = {
    "check_heartbeat_every_5_second": {
        "task": "jobs.tasks.heartBeat",
        "schedule": 5.0,
        "name": "heartbeat",
    }
}
