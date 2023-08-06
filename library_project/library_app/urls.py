from django.urls import path
from library_app import views
urlpatterns=[
    path('', views.redirect_to_book_name),
    path('<str:filter>/',views.index,name='index'),
    path('add_info/add_author/',views.add_author,name='add_author'),
    path('add_info/add_genre/',views.add_genre,name='add_genre'),
    path('add_info/add_book/',views.add_book,name='add_book'),
    path('book/<int:id>/',views.single_book,name='single_book'),
    path('author/<int:id>/',views.single_author,name='single_author'),



]