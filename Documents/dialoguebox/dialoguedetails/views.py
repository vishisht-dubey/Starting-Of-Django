from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Vishisht, You created your first django project")
