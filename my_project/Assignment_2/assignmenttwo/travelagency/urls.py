from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . views import login_view, logout_view, register_view, hi

urlpatterns = [
    path('', login_view, name='login'),
    path('chatbot/', hi, name='chatbot'),
    path('logout/', logout_view),
    path('register/', register_view)
]
urlpatterns += staticfiles_urlpatterns()
