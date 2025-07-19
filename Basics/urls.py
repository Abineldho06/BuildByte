from django.urls import path,include
from Basics import views

urlpatterns = [
   path('Calculator/',views.calculation,name='Calculator'),
   path('Add/',views.add,name='add'),
   path('Largest',views.largest,name='Largest'),
]
