import os
from django.core import management
from django.conf import settings
from django_cron import CronJobBase, Schedule


class Backup(CronJobBase):
    RUN_EVERY_MINS = 1
    RUN_AT_TIMES = ['6:00', '18:00']
    schedule = Schedule(run_every_mins = RUN_EVERY_MINS)
    code = 'my_app.Backup'

    def do(self):
        management.call_command('dbbackup')