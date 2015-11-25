from django.shortcuts import render
from .models import *

#This is Nathan's code. You can probably tell because there are too many comments.

# Create your views here.
def index(request):
  return HttpResponse('<h1>Home Page</h1>')
  
def quiz_overview(request,quiz_id):
  #Example of a procedurally constructed (as opposed to templated) view.

  #Sanity check on the input. We want to make sure we're querying an actual quiz -- if we're not, big trouble!!!
  try:
  	quiz = Quiz.objects.get(id=quiz_id)
  except Quiz.DoesNotExist:
  	return HttpResponseNotFound("<h1>That quiz does not exist.</h1>")

  html = "<h1>Quiz Overview</h1>"
  return HttpResponse(html)