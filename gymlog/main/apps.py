from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'gymlog.main'
    verbose_name = "Main"

    def ready(self):
        """Override this to put in:
            Main system checks
            Main signal registration
        """
        pass
