from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Group, Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            "id",
            "title",
            "slug",
            "description",
        )


class CommentSerializer(serializers.ModelSerializer):

    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "author", "text", "created", "post")

        read_only_fields = ("author", "post")


class PostSerializer(serializers.ModelSerializer):

    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Post
        fields = ("id", "text", "author", "group", "pub_date", "image")
