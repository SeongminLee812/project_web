from django.shortcuts import render

# Create your views here.
def kocw(request):
    return render(request, 'kocw.html')