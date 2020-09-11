from django.urls import path
from level_two_app import views

urlpatterns = [
    path('',views.index),
    path('users/',views.users),
    path('formpage/',views.form_name_view),

]
