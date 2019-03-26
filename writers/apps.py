from django.apps import AppConfig


class WritersConfig(AppConfig):
    name = 'writers'

    def ready(self):
        import writers.signals
