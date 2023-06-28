import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):  #Aqui se ponen los modelos o clase... no hace falta crear un id, django lo crea automáticamente
    question_text = models.CharField(max_length=200) #QAquí tenemos atributo de la clase y CharField es un tipo de dato que se puede utilizar para un atributo.(varchar)
    pub_date = models.DateTimeField("date published") #Fecha de publicación

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model): #id automática
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #question es la llave foranea que hace que cada uno de los registros corresponda a una pregunta... relación uno a muchos
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) #Campos de números enteros
    #ON_dELETE=MODELS.cascade QUIERE DECIR QUE CADA VEZ que borremos una pregunta, se vana borrar todas las chices o respuestas que tenga.

    def __str__(self):
        return self.choice_text

# Create your models here.
