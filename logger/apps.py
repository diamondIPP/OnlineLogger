from django.apps import AppConfig
from django.utils.autoreload import autoreload_started
from pathlib import Path
from os.path import join, realpath, dirname


def my_watchdog(sender, **kwargs):
    _ = kwargs
    sender.extra_files.add(Path(join(dirname(dirname(realpath(__file__))), 'config', 'config.ini')))


class LoggerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'logger'

    def ready(self):
        autoreload_started.connect(my_watchdog)
