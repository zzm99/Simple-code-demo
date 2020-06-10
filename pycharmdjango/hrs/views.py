# Create your views here.
from django.shortcuts import render
from hrs.models import Teacher, Subject
from django.http import HttpResponse,JsonResponse

def show_subjects(request):
    """查看所有学科"""
    subjects = Subject.objects.all()
    return render(request, 'index.html', {'subjects': subjects})

def show_teachers(request):
    """查看指定学科的老师"""
    try:
        sno = int(request.GET['sno'])
        subject = Subject.objects.get(no=sno)
        teachers = Teacher.objects.filter(subject__no=sno)
        context = {'subject': subject, 'teachers': teachers}
        return render(request, 'teacher.html', context)
    except (KeyError, ValueError, Subject.DoesNotExist):
        return redirect('/')

def praise_or_criticize(request):
    """好评"""
    try:
        tno = int(request.GET['tno'])
        teacher = Teacher.objects.get(no=tno)
        if request.path.startswith('/praise'):
            teacher.good_count += 1
        else:
            teacher.bad_count += 1
        teacher.save()
        data = {'code': 200, 'hint': '操作成功'}
    except (KeyError, ValueError):
        data = {'code': 404, 'hint': '操作失败'}
    return JsonResponse(data)

