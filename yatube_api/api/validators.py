# api/validators.py
from rest_framework.exceptions import ValidationError


class VariousValidator:
    requires_context = True

    def __call__(self, attrs, serializer):
        follower = serializer.context["request"].user.username
        following = serializer.initial_data["following"]

        if follower == following:
            message = "Вы не можете подписатся на себя."
            raise ValidationError(message, code="various")
