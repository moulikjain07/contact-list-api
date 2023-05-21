from django.urls import path
from .views import *

urlpatterns = [
    path('list/', ContactList.as_view()),
    path('', ContactCreate.as_view()),
    path('<int:pk>', ContactDetail.as_view())
]