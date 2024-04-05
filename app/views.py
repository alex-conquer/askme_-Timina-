from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
QUESTIONS = [
    {
        "id": i,
        "title": f"Question {i}",
        "text": f"This is question number {i}"
    } for i in range(200)
]

def index(request):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(QUESTIONS, 5)
    page_obj = paginator.page(page_num)
    return render(request, "index.html", {"questions": page_obj})


def hot(request):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(QUESTIONS[5:],5)
    page_obj = paginator.page(page_num)
    return render(request, "hot.html", context={"questions": page_obj})


def question(request, question_id):
    item = QUESTIONS[question_id]
    return render(request, template_name="question_detail.html", context={"question": item})

def ask(request):
    return render(request, "ask.html")

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

def settings(request):
    return render(request, "settings.html")

def tag(request):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(QUESTIONS[5:],5)
    page_obj = paginator.page(page_num)
    return render(request, template_name="TegsListQuestion.html", context={"question":page_obj})

def blablabla(request):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(QUESTIONS[5:],5)
    page_obj = paginator.page(page_num)
    return render(request, template_name="blablabla.html", context={"question":page_obj})