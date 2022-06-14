from apps.stackoverflow.models import Answer

from rest_framework import serializers


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        exclude = ("question",)
