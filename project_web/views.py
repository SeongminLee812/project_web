from django.shortcuts import render
from .forms import MyMemberForm

def index(request):
    return render(request, 'project_index.html')

# 테스트
def test(request):
    pass

def register(request):
    return render(request, 'register.html', {'form': MyMemberForm()})
