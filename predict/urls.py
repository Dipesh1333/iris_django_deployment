from django.urls import path
from . import views

app_name = 'predict'   #the 'predict' is from the namespace in urls.py

urlpatterns = [
    path('', views.predict, name='predict'),
    path('predict/', views.predict_chances, name = 'submit_prediction'),
]