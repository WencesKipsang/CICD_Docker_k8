from django.urls import path
from cicd import views

urlpatterns = [
    path('heyai/', views.home ,name = 'welcome'),
]