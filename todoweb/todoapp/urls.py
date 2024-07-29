from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from. import views

urlpatterns = [
    path("",views.home,name="home"),
    path("todo/",views.todo,name="todo"),
    path("about/",views.about,name="about"),
    path("add_todo",views.add_todo,name="add_todo"),
    path("delete/<int:todo_id>",views.delete,name="delete"),
    path("update_todo/<int:todo_id>",views.update_todo,name="update_todo"),
    path("complete/<int:todo_id>",views.complete,name="complete"), 
    path("profile",views.profile,name="profile"),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

