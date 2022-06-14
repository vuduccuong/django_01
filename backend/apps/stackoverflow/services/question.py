from apps.stackoverflow.models import Question


class QuestionServices():

    @classmethod
    def list(cls):
        return Question.objects.prefetch_related("answers").all()

    @classmethod
    def detail(cls, pk: int):
        return Question.objects.get(pk=pk)
