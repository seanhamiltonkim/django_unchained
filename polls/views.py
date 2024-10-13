from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db import connection

from .models import Question

def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    return render(request, "polls/index.html", {
        "latest_questions_list": latest_questions
    })

def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    key = "question"
    return render(request, "polls/detail.html", {key: question})

def results(request, question_id):
    response = "Result of question #%s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse(f"Voting on #{question_id}")
