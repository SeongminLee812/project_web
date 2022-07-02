from django.shortcuts import render
from .models import MoocAllList
from django.db.models import Q # or문 사용하기 위해 import 함
from django.db.models import Count # 중복개수 세기 위해 import 함

# Create your views here.
def kmooc(request):
    return render(request, 'kmooc.html')

def kmooc_data(request):
    course_list = MoocAllList.objects.filter(Q(fourth_industry_yn='y')|Q(ai_sec_yn='y')) #.order_by('-star')[:10]    #or 조건문
    print(course_list)
    # 중복 있는 이름들만 구하기
    duplicate_names = course_list.values('name').annotate(name_count=Count('name')).filter(name_count__gt=1)

    print(duplicate_names)
    return render(request, 'kmooc.html', {'MoocAllList':course_list})
    #MoocAllList(html에 전달할 값)에 위 course_list변수

# test__