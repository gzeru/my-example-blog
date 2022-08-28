#from django.shortcuts import render

#from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at the myblog index.")






from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from . import views

#from .models import Question


def index(request):
#   latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('myblog/index.html')
    template = "myblog/index.html"
    #context = {
    #    'latest_question_list': latest_question_list,
    #}
#    return HttpResponse(template.render(context, request))

    context = {
     'test': "my test"
    }

 #   return HttpResponse(template.render())
    return render(request,template)