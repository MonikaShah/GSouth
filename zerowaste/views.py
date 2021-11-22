from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect

# Create your views here.
def HomePage(request):
    return render(request,"HomePage.html")