from django.shortcuts import render
from .forms import MyMemberForm
import os
from kmooc.models import MoocAllList
from kocw.models import KocwAllList
from edwith.models import EdwithAllList
from django.db.models import Q
import pandas as pd
import datetime

def index(request):
    today = datetime.datetime.now()
    print(today)
    course_list = MoocAllList.objects.filter((Q(fourth_industry_yn='y')|Q(ai_sec_yn='y'))&Q(middle_classfy='comp')&(Q(audit_yn='y')|Q(enrollment_end__gte=today))).order_by('-star')  #or 조건문
    # 중복제거 코드
    # 판다스 데이터 프레임 이용
    df = pd.DataFrame(list(course_list.values()))
    # 이름(name 컬럼의 값)이 같은 값 제거하면서 첫번째 값만 남기기
    df = df.drop_duplicates(subset="name", keep="first")
    not_dup_course_list = list()
    # 10개만 뽑을 거니까 10번만 반복해서 list에 추가
    for i in range(3):
        not_dup_course_list.append(df.iloc[i])
    course_kmooc = not_dup_course_list
    course_kocw = KocwAllList.objects.all().order_by('-view_count')[:3]
    course_edwith = EdwithAllList.objects.all().order_by('-like_num')[:3]
    return render(request, 'project_index.html', {'moocpop01': course_kmooc[0], 'moocpop02': course_kmooc[1], 'moocpop03': course_kmooc[2],
                                                  'kocwpop01': course_kocw[0], 'kocwpop02': course_kocw[1], 'kocwpop03': course_kocw[2],
                                                  'edwithpop01': course_edwith[0],'edwithpop02': course_edwith[1], 'edwithpop03': course_edwith[2],
                                                  })


# 테스트
def test(request):
    pass

def register(request):
    return render(request, 'register.html', {'form': MyMemberForm()})


def search(request):
    search_word = request.POST['q']
    # 검색어가 여러개일 경우
    search_word_split = search_word.split(' ')
    if len(search_word_split) > 1:
        search_result_kmooc = MoocAllList.objects.filter(Q(name__contains=search_word_split[0])|Q(name__contains=search_word_split[1])).order_by('-enrollment_start')
        search_result_kocw = KocwAllList.objects.filter(Q(course_title__contains=search_word_split[0])|Q(course_title__contains=search_word_split[1]))
        search_result_edwith = EdwithAllList.objects.filter(Q(title__contains=search_word_split[0])|Q(title__contains=search_word_split[1]))
    # post방식으로 전달된 값 받아서 포함하는 값들만 가져옴 (icontains는 대소문자 무시)
    # 각 데이터 베이스마다 이름을 나타내는 컬럼명이 다르므로, 각각 따로 검색 기능 구현함

        # kmooc 중복제거
        df = pd.DataFrame(list(search_result_kmooc.values()))
        df = df.drop_duplicates(subset='name', keep='first')
        search_kmooc_dict_list = df.to_dict('records')

    else:
        search_result_kmooc = MoocAllList.objects.filter(name__contains=search_word).order_by('-enrollment_start')
        search_result_kocw = KocwAllList.objects.filter(course_title__contains=search_word)
        search_result_edwith = EdwithAllList.objects.filter(title__contains=search_word)

        df = pd.DataFrame(list(search_result_kmooc.values()))
        df = df.drop_duplicates(subset='name', keep='first')
        # K-MOOC star nan -> '-'
        df = df.fillna('-')
        search_kmooc_dict_list = df.to_dict('records')

        #KOCW popular_score None -> '-'
        for course in search_result_kocw:
            if course.popular_score is None:
                course.popular_score = '-'


    return render(request, 'search.html', {'searchResultKmooc': search_kmooc_dict_list,
                                           'searchResultKocw': search_result_kocw,
                                           'searchResultEdwith': search_result_edwith,
                                           'kmooc_num': len(search_kmooc_dict_list),
                                           'kocw_num': len(search_result_kocw),
                                           'edwith_num': len(search_result_edwith)})
