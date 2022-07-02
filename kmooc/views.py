from django.shortcuts import render
from .models import MoocAllList
from django.db.models import Q # or문 사용하기 위해 import 함
from django.db.models import Count # 중복개수 세기 위해 import 함\
from django.db.models import QuerySet
import pandas as pd

# Create your views here.
def kmooc(request):
    return render(request, 'kmooc.html')

def kmooc_data(request):

    course_list = MoocAllList.objects.filter(Q(fourth_industry_yn='y')|Q(ai_sec_yn='y')).order_by('-star')  #or 조건문
    # 중복제거 코드
    # 판다스 데이터 프레임 이용
    df = pd.DataFrame(list(course_list.values()))
    # 이름(name 컬럼의 값)이 같은 값 제거하면서 첫번째 값만 남기기
    df = df.drop_duplicates(subset="name", keep="first")
    not_dup_course_list = list()
    # 10개만 뽑을 거니까 10번만 반복해서 list에 추가
    for i in range(10):
        not_dup_course_list.append(df.iloc[i])
    print(not_dup_course_list)

    return render(request, 'kmooc.html', {'MoocAllList':not_dup_course_list})
    #MoocAllList(html에 전달할 값)에 위 course_list변수