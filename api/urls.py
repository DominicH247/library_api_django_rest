from django.urls import path

from.views import BookAPIView

urlpatterns = [
	path('', includes, BookAPIView.as_view()),

]