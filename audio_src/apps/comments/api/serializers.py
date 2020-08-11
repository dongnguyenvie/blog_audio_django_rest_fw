from rest_framework import serializers
from audio_src.apps.comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    article_thumbnail = serializers.StringRelatedField(
        source='article.thumbnail', read_only=True)
    article_slug = serializers.StringRelatedField(
        source='article.slug', read_only=True)

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ['isDeleted']
