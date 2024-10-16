from django.apps import AppConfig


class FeastoCoreAppConfig(AppConfig):
    name = "feasto_core"

    def ready(self):
        from feasto_core import signals # pylint: disable=unused-variable
