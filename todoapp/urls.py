from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('edit_todo/<int:pk>/', views.edit_todo, name='edit_todo'),
    path('itemdelete/<int:pk>/', views.itemdelete, name='itemdelete'),
    path('markdone/<int:pk>/', views.markdone, name='markdone'),
    # path('itemupdate/<int:pk>/', views.itemupdate, name='itemupdate'),
]
