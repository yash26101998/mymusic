from django.urls import path
from . import views
urlpatterns = [
    path('',views.render_signinpage,name='render_signinpage')
    
]
