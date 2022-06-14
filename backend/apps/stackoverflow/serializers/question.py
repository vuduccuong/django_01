from apps.stackoverflow.models import Question
from rest_framework import serializers

from apps.stackoverflow.serializers.tag import TagSerializer
from apps.stackoverflow.serializers.answer import AnswerSerializer


class QuestionSerializer(serializers.ModelSerializer):

    tags = TagSerializer(read_only=True, many=True)
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = "__all__"
