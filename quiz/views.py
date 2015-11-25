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
  	#Django has a bunch of built in HTTP headers for different errors. This is the 404 header.
  	return HttpResponseNotFound("<h1>That quiz does not exist.</h1>")

  html = "<h1>Quiz Overview for" + quiz.title + "</h1>"

  #This is a generic HTTP response header. Just like with the 404, the page code is sent as a string.
  return HttpResponse(html)