from django.apps import AppConfig


class PostsConfig(AppConfig):
    name = 'audio_src.posts'

    def ready(self):
        import posts.signals  # pylint: disable=import-outside-toplevel,unused-import
