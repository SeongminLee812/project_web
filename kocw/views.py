from django.shortcuts import render
from .models import KocwAllList

# Create your views here.
def kocw(request):
    return render(request, 'kocw.html')

def kocw_data(request):
    course_list = KocwAllList.objects.all().order_by('-view_count')[:10]  #or 조건문
    return render(request, 'kocw.html', {'KocwAllList':course_list})

# test
def test():
    pass