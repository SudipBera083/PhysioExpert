
from django.urls import path
from .views import index,submit_review, book_appointment
app_name = "main"

urlpatterns = [
    path('',index, name='mainPage'),
    path('submit_review/', submit_review, name= 'submit'),
    path('book-appointment/', book_appointment, name='book_appointment'),
]