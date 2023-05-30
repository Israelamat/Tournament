from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('accountcreated/', views.account_created, name="accountcreated")
]