
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('result/<str:task_id>', views.check_result, name='check_result'),

    #Student Api
    path('api/students/', views.StudentView.as_view()),
    path('api/students/<int:id>/', views.StudentView.as_view()),

]
