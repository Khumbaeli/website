from django.shortcuts import render

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def photography(request):
    context = {
        "title": "Photography",
    }
    return render(request, "Photography.html", context)

def climbing(request):
    context = {
        "title": "Climbing",
    }
    return render(request, "climbing.html", context)

def project(request):
    context = {
        "title": "Projects",
    }
    return render(request, "project.html", context)



