from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, "index.html")

def results(request):
    context = {
        'name' : request.POST["name"],
        'location'	: request.POST['location'],
        'language'	: request.POST['language'],
        'comments'  : request.POST['comments'],
    }
    if request.method=="POST":
        name = request.POST["name"]
        location = request.POST["location"]
        language = request.POST["language"]
        comments = request.POST["comments"]
    return render(request, "results.html", context)
