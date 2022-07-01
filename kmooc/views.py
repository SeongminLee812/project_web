from django.shortcuts import render

# Create your views here.
def kmooc(request):
    return render(request, 'kmooc.html')