from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_plans, name='all_plans'),
    path('<name>', views.individual_plan, name='individual_plan'),
]
