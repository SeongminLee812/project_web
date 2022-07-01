from django.shortcuts import render
from .models import MoocAllList

# Create your views here.
def kmooc(request):
    return render(request, 'kmooc.html')

def kmooc_data(request):
    course_list = MoocAllList.objects.filter(fourth_industry_yn='y')
    return render(request, 'kmooc.html', {'MoocAllList':course_list})
    #MoocAllList(html에 전달할 값)에 위 course_list변수
