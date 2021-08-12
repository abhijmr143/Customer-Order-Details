from django.urls import path
from . import views

app_name = 'myApps'


urlpatterns = [
    path('', views.list_view, name='list'),
    path('create/', views.create_list, name='create'),
    path('update/<int:pk>/', views.update_list, name='update'),
    path('delete/<int:pk>/', views.delete_list, name='delete'),
    path('graph/', views.visualization_view, name='graph'),
]