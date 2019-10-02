from django.shortcuts import render

def index(req):
    context = {

    }
    return render(req,"presence/index.html",context=context)
