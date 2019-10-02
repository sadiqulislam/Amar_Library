from django.shortcuts import render

#1
def index(req):
    context = {

    }
    return render(req,"presence/index.html",context=context)
#2
def home(req):

    context={

    }
    return render(req,"presence/home.html",context=context)
#3
def book_list(req):

    context={

    }
    return render(req,"presence/book_list.html",context=context)
#4
def member_list(req):

    context={

    }
    return render(req,"presence/member_list.html",context=context)

#5
def add_book(req):
    context={

    }
    return render(req,"presence/add_book.html",context=context)

#6
def about(req):
    context={

    }
    return render(req,"presence/about.html",context=context)


