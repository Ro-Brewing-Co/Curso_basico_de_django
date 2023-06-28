from django.urls import path 

from . import views

app_name = "polls"

urlpatterns = [
    #example: /polls/
    path("", views.IndexView.as_view(), name="index"),
    #example: /polls/5/ voy a poder accceder al detalle de la pregunta número 5
    #el int quiere decir entero u questio_id el id de cada pregunta
    #views.details quiere decir que se utiliza la función detail del módulo views
    path("<int:pk>/detail/", views.DetailView.as_view(), name="detail"),
    #example: /polls/5/results
    path("<int:pk>/results/", views.ResultView.as_view(), name="results"),
    #example: /polls/5/vote
    path("<int:question_id>/vote/", views.vote, name="vote"),
]