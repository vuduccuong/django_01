from django.urls import path, include

from rest_framework import routers

from apps.stackoverflow.views.question import QuestionViewSet

router = routers.SimpleRouter()
router.register(r'questions', QuestionViewSet, basename='stackoverflow_question')

urlpatterns = [
    path('', include(router.urls))
]
