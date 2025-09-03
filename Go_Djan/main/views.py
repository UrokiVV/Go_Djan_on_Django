from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    s1 = "<h1>Это новый проект Go_Djan</h1>"
    s2 = "<h2>Проект Go_Djan разработан на Django</h2>"
    s3 = "<h3>Это - только начало </h3>"
    return HttpResponse(s1 + s2 + s3)


def newtest(request):
    s1 = "<h1>Вторая страница 'newtest' проекта Go_Djan</h1>"
    s2 = "<h2>Проект Go_Djan разработан на Django</h2>"
    s3 = "<h3>Проба пера... Проба... </h3>"
    return HttpResponse(s1 + s2 + s3)


def data(request):
    s1 = "<h1>Третья страница 'data' проекта Go_Djan</h1>"
    s2 = "<h2>Проект Go_Djan разработан на Django</h2>"
    s3 = "<h3> и так далее...</h3>"
    return HttpResponse(s1 + s2 + s3)
