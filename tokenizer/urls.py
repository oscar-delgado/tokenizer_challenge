from django.urls import path

from tokenizer import views

urlpatterns = [
    path('tokenizer/', views.tokenizer, name="tokenizer")
]
