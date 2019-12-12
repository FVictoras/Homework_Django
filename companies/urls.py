from django.urls import path
from companies import views

app_name = 'company'

urlpatterns = [
    path('', views.CompaniesIndex.as_view(), name='index'),
    # path('read/<int:pk>/', views.ReadIndex.as_view(), name='read'),
    path('delete/<int:pk>/', views.DeleteCompanyView.as_view(), name='remove_company'),
    path('update/<int:pk>/', views.UpdateCompanyView.as_view(), name='update_company'),
    path('add/', views.CreateCompanyView.as_view(), name='create_company'),
    ]

