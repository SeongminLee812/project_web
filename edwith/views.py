from django.shortcuts import render
from .models import EdwithAllList

# Create your views here.
def edwith_visual(request):
    course_list01 = EdwithAllList.objects.all().order_by('-like_num')[:10]
    course_list02 = EdwithAllList.objects.all().order_by('-like_num')[:10]

    return render(request, 'edwith.html', {'EdwithAllList': course_list01})

# GIT TEST ID