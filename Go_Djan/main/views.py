# main\views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):  # главная стр
    return render(request, 'main/index.html')


def newtest(request):   # вторая стр
    return render(request, 'main/newtest.html')


def data(request):     # третья стр
    return render(request, 'main/data.html')


def next04(request):     # четвёртая стр
    return render(request, 'main/next04.html')


def about(request):     # Подвал
    return render(request, 'main/footer.html')


def new(request):
    return render(request, 'main/new.html')


def index01(request):
    s1 = "<h1>Это новый проект Go_Djan</h1>"
    s2 = "<h2>Проект Go_Djan разработан на Django</h2>"
    s3 = "<h3>Страница 'index01' - это только начало </h3>"
    return HttpResponse(s1 + s2 + s3)


def newtest01(request):
    s1 = "<h1>Вторая страница 'newtest01' проекта Go_Djan</h1>"
    s2 = "<h2>Проект Go_Djan разработан на Django</h2>"
    s3 = "<h3>Проба пера... Проба... </h3>"
    return HttpResponse(s1 + s2 + s3)


def data01(request):
    s1 = "<h1>Третья страница 'data01' проекта Go_Djan</h1>"
    s2 = "<h2>Проект Go_Djan разработан на Django</h2>"
    s3 = "<h3> и так далее...</h3>"
    return HttpResponse(s1 + s2 + s3)
