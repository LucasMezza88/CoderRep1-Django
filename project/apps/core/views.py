from django.shortcuts import render

def index(request):
    context = {"app_name": "Coderhouse"}
    return render(request, "core/index.html", context)
