from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):

    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'elections/questions_list.html', context)

    # return HttpResponse("Hello World!!")

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context={'question': question}

    print(render(request, 'elections/question_detail.html', context))
    return render(request, 'elections/question_detail.html', context)


def test(request):
    list = ["str \n","str \n","str \n","str \n","str \n",]
    return HttpResponse(list)


