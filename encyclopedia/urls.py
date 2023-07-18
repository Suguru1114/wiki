from django.urls import path

from . import views

from encyclopedia import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("add/", views.add_page, name="add_page"),
    # path("wiki/<str:title>/edit", views.edit_page, name="edit_page"),
    path("edit/", views.edit_page, name="edit"),
    path("save_edit/", views.save_edit,name="save_edit"),
    path("rand/", views.rand, name="rand")
    
 ]
  