from django.shortcuts import render, redirect, HttpResponse


def index(request):
    return render(request, "index.html")

# def results(request):
# Keeping this for posterity
#     # request.session['name'] = request.POST['name']
#     # request.session['location'] = request.POST['location']
#     # request.session['language'] = request.POST['language']
#     # request.session['comments'] = request.POST['comments']
#     # if request.method=="POST":
#     #     name = request.POST["name"]
#     #     location = request.POST["location"]
#     #     language = request.POST["language"]
#     #     comments = request.POST["comments"]
#     return render(request, "/results.html")


def session_items(request):
    request.session['results'] = {
        'name': request.POST['name'],
        'location': request.POST['location'],
        'language': request.POST['language'],
        'comments': request.POST['comments'],
    }
    return redirect('/results')


def results(request):
    context = {  # context could be anything as long as we call it below
        'results': request.session['results']
    }
    return render(request, "results.html", context)  # see context here!
