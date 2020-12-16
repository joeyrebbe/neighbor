from django.shortcuts import render

# Create your views here.


def home(request):
  return render(request, 'home.html') 

  # Define the ABOUT/ view
# def about(request):
#   return HttpResponse('<h1>This is About Page</h1>') # simmiluar to res.send

def about(request):
    return render(request, 'about.html') #instead of HTTPResponse we can use a template