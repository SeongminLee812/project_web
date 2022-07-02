from django.shortcuts import render
from .forms import MyMemberForm
import os
from kmooc.models import MoocAllList
from kocw.models import KocwAllList
from edwith.models import EdwithAllList

def index(request):
    return render(request, 'project_index.html')

# 테스트
def test(request):
    pass

def register(request):
    return render(request, 'register.html', {'form': MyMemberForm()})


def search(request):
    search_word = request.POST['q']

    # post방식으로 전달된 값 받아서 포함하는 값들만 가져옴 (icontains는 대소문자 무시)
    # 각 데이터 베이스마다 이름을 나타내는 컬럼명이 다르므로, 각각 따로 검색 기능 구현함
    search_result_kmooc = MoocAllList.objects.filter(name__icontains=search_word)
    search_result_kocw = KocwAllList.objects.filter(course_title__icontains=search_word)
    search_result_edwith = EdwithAllList.objects.filter(title__icontains=search_word)
    return render(request, 'search.html', {'searchResultKmooc': search_result_kmooc,
                                           'searchResultKocw': search_result_kocw,
                                           'searchResultEdwith': search_result_edwith})
