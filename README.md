# Celery and scheduler (redBeat)

`poetry install`

run:

terminal 1:
`celery -A jobs.worker worker -l debug`

terminal 2:
`celery -A jobs.worker beat -l debug`

terminal 3:
`celery -A jobs.worker flower --port=5556`

terminal 4:

run a python shell:

- add task:

```
from jobs.worker import *
dummy_scheduled_task.delay()
```

- delete task:

```
delete_task("readbeatcheck_heartbeat_every_5_second")
```

Important notes:

- with every changes, we should restart worker and python shell
