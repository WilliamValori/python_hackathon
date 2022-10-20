from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

# from .models import Question


# def index(request):
#     return HttpResponse("Hello, world. You're at the meat up!.")
from smoke_generator.models import Recipe


def index(request):
    latest_question_list = ["Heb je trek?", "Wat gaat erop?"]
    template = loader.get_template('smoke_generator/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def recipe(request):
    return HttpResponse("The recipe name is spare_ribs")

def test(request):
    obj = Recipe.objects.all()

    context = {"object": obj}

    return render(request, "page2.html",context)
 