from django.shortcuts import render

# Create your views here.
def render_signinpage(request):
    return render(request,'signin.html')
