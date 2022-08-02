from checks import views
from django.urls import path

app_name = 'checks'

urlpatterns = [
    path('', views.checks, name='checks'),
]