from django.http import Http404
from django.shortcuts import get_object_or_404, render 
from django.http import HttpResponse
#from django.template import loader

from .models import Question

# Create your views here.
def index(request):
    # 3rd try: use 'render' to call request, template; skip loader/httpResponse
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    # 1st try: text with formatting here in python function
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    # 2nd try: set up a template and use loader/httpResponse
    #template = loader.get_template('polls/index.html')
    #context = {
    #    'latest_question_list': latest_question_list,
    #}
    #return HttpResponse(template.render(context, request))
    
def detail(request, question_id):
    # 3rd try: shortcut with get_object_or_404()
    question = get_object_or_404(Question, pk=question_id)
    
    # 2nd try: with raiseHttp404 explicit
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist.")
    return render(request, 'polls/detail.html', {'question': question})
    
    # original view, with simple view
    #return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of the question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

