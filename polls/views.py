from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic

'''
def index(request):
    latest_question_list = Question.objects.all() #Con esto se obtiene un objeto tipo queryst con todas las preguntas las cuales se guardan en la variable latest...
    return render(request, "polls/index.html", {
                  "latest_question_list": latest_question_list #Aquí van variables que puedan ser usadas por la template esto en un diccionario
    })   #HttpResponse("Estás en la página principal de Premios Platzi App")...render pide 3 parámetros... un requerimiento request, el template de polls/index.html en la carpeta de template y polls

def  detail(request, question_id):  #vista de las preguntas y diferentes opciones de respuesta Recibe un requerimiento y como segundo parámetro recibe la llave primaria de la pregunta que nosotros queremos mostrar
# Create your views here.
    question = get_object_or_404(Question, pk=question_id)        #Si se obtiene Question se guarda en question o sino, da un error 404
    return render(request, "polls/detail.html", {
        "question": question
    })
    # 
    # 
    # return HttpResponse(f"Estas viendo la pregunta número {question_id}")  #Esto es para mostrar el mensaje de f y la pregunta por id

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {
        "question": question
    })
    #Después de ejecutar vote se ejecuta results 
    # 
    # return HttpResponse(f"Estás viendo los resultados de la pregunta número {question_id}")
'''

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

    

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "No elegiste una respuesta"
        })
    else: 
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))

    # 
    # return HttpResponse(f"Estás votando a l pregunta número {question_id}")

'''
La primera función nombrada como index es una buena práctica. Luego, las deás funciones son vistas que
deben ser puestas en el archivo de las urls.py del módulo polls...
'''