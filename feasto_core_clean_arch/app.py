from django.apps import AppConfig


class FeastoCoreCleanArchAppConfig(AppConfig):
    name = "feasto_core_clean_arch"

    def ready(self):
        from feasto_core_clean_arch import signals # pylint: disable=unused-variable
