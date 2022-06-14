from django.db import models

from apps.core.models.base import Authorable, Timestampable
from .question import Question


class Answer(Authorable, Timestampable):
    answer = models.TextField()
    question = models.ForeignKey(
        Question, related_name="answers", on_delete=models.CASCADE)

    class Meta:
        db_table = 'stackoverflow_answers'
