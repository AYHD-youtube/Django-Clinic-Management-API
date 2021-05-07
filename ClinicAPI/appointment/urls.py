from django.urls import path
from .views import Calender, Login, BookAppointment,Register


urlpatterns = [
    path('register', Register.as_view(), name='Register'),
    path('login', Login.as_view(), name='Login'),
    path('calender', Calender.as_view(), name='set-calender'),
    path('book-appointment', BookAppointment.as_view(), name='book-appointment'),
]
