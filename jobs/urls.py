from django.urls import path

from jobs import views

app_name = 'jobs'

urlpatterns = [
    path('', views.JobsIndex.as_view(), name='index'),
    #  path('read/<int:pk>/', views.ReadIndex.as_view(), name='read'),
    path('delete/<int:pk>/', views.DeleteJobsView.as_view(), name='remove_job'),
    path('update/<int:pk>/', views.UpdateJobsView.as_view(), name='update_job'),
    path('add/', views.CreateJobsView.as_view(), name='create_jobs')
    ]
