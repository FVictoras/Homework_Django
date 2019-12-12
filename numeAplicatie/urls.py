from django.urls import path
from numeAplicatie import views

app_name = 'app1'

urlpatterns = [
    path('', views.HomeIndex.as_view(), name='home'),
    # path('read/<int:pk>/', views.ReadIndex.as_view(), name='read'),
    path('update/<int:pk>/', views.UpdateIndex.as_view(), name='update'),
    path('add_location/', views.CreateLocation.as_view(), name='add_new_location'),
    ]

