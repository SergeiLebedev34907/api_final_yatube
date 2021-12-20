# api/serializers.py
from rest_framework import serializers, validators
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post, User

from .validators import VariousValidator


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "slug", "title", "description")


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = ("id", "author", "text", "pub_date", "image", "group")
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ("id", "author", "text", "created", "post")
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="username"
    )
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        fields = ("user", "following")
        model = Follow

        validators = [
            validators.UniqueTogetherValidator(
                queryset=Follow.objects.all(), fields=("user", "following")
            ),
            VariousValidator(),  # , values=(user, following)
        ]
