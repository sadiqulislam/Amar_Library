from django.urls import path
from .views import (
    index,
    home,
    book_list,
    member_list,
    add_book,
    about,

)


urlpatterns = [

    path("",index,name='index'),
    path("Home.py",home,name="home"),
    path("Book-List.py",book_list,name="book-list"),
    path("Member-List.py",member_list,name="member-list"),
    path("Add-Book.py",add_book,name="add-book"),
    path("About-Us.py",about,name="about")
]