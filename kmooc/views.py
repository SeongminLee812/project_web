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


    # course_list = MoocAllList.objects.distinct().value_list('name', 'fourth_industry_yn', 'ai_sec_yn', 'course_id', 'star')


    '''
    # print(course_list, '\n\n\n')
    # 중복 있는 이름들만 구하기
    duplicate_names = course_list.values('name').annotate(name_count=Count('name')).filter(name_count__gt=1)
    # duplicate_name을 활용해서 이름 리스트를 만들기
    dup_name_list = list()
    for i in range(len(duplicate_names)):
        dup_name_list.append(duplicate_names[i]['name'])
    print(dup_name_list)

    # course_list 반복문 돌리면서 이름이 duplicate_name에 있는 지 판단, 없는 것만 추가 ()
    not_dup_course_list = list()
    for i in course_list:
        if i.name not in dup_name_list:
            not_dup_course_list.append(i)
    '''


    # for i in course_list:
    #     for j in range(len(duplicate_names)):
    #         if i.name == duplicate_names[j]['name']:
    #             dup_list.append(i)
    # print(not_dup_list[:10], '\n\n\n')
    # group_by로 해결해보기
    '''
    query = MoocAllList.objects.all().query
    query.group_by = ['name']
    results = QuerySet(query=query, model=MoocAllList)
    print(results.order_by('-star')[:10])'''

    return render(request, 'kmooc.html', {'MoocAllList':not_dup_course_list})
    #MoocAllList(html에 전달할 값)에 위 course_list변수

# test__