from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.add_student, name='student'),
    path('list/', views.show_list, name='list'),

    # path('items/', views.item_list, name='item'),
    # Add more URL patterns for your views here
]
