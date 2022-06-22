from django.shortcuts import render

# Create your views here.
def render_signuppage(request):
    return render(request,'signup.html')
