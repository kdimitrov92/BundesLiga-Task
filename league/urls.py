from django.urls import path

from league.views import Home


urlpatterns = [
    path('', Home.as_view()),
]
