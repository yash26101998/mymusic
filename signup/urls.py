from django.urls import path
from . import views

urlpatterns = [
    path('',views.render_signuppage,name='render_signuppage'),
]
