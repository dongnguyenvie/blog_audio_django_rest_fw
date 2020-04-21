from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'customers'
    def ready(self):
        import customers.signals  # pylint: disable=import-outside-toplevel,unused-import