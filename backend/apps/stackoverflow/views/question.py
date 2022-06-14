from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.core.constants.view_sets import AppViewSet
from apps.stackoverflow.services.question import QuestionServices
from apps.stackoverflow.serializers.question import QuestionSerializer


class QuestionViewSet(viewsets.ViewSet):
    view_set = AppViewSet.STACKOVERFLOW_QUESTION

    def list(self, request):
        questions = QuestionServices.list()
        serializer = QuestionSerializer(questions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        question = QuestionServices.detail(pk=pk)
        serializer = QuestionSerializer(question)

        return Response(serializer.data, status=status.HTTP_200_OK)