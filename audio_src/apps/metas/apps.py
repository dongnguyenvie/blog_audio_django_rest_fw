from django.apps import AppConfig


class MetaConfig(AppConfig):
    name = 'apps.metas'

    def ready(self):
        import metas.signals  # pylint: disable=import-outside-toplevel,unused-import
