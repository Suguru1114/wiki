from django.urls import path

from . import views

from encyclopedia import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    # path('entry/<str:title>/', views.entry, name='entry'),
    # path('entry/<str:title>/', views.entry_page, name='entry'),
    # path('error/', views.error_page, name='error'), 
    # from stackoverflow
    path("search/", views.search, name="search"),
    
 ]
  