from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Classz, Student
from django.template import loader

def index(request):
    all_classzes = Classz.objects.all()
    return render(request, 'student/index.html', {'all_classzes':all_classzes})

def grace(request):
    all_classzes1 = Classz.objects.filter(pk=1)
    all_classzes2 = Classz.objects.filter(pk=2)
    all_classzes3 = Classz.objects.filter(pk=3)
    all_classzes4 = Classz.objects.filter(pk=4)

    all_students_in_classz1 = Student.objects.filter(classz_id=1)
    all_students_in_classz2 = Student.objects.filter(classz_id=2)
    all_students_in_classz3 = Student.objects.filter(classz_id=3)
    all_students_in_classz4 = Student.objects.filter(classz_id=4)

    template = loader.get_template('student/grace.html')
    context = {
        'all_classzes1': all_classzes1,
        'all_classzes2': all_classzes2,
        'all_classzes3': all_classzes3,
        'all_classzes4': all_classzes4,

        'all_students_in_classz1': all_students_in_classz1,
        'all_students_in_classz2': all_students_in_classz2,
        'all_students_in_classz3': all_students_in_classz3,
        'all_students_in_classz4': all_students_in_classz4
    }
    return HttpResponse(template.render(context, request))

def face(request):

    all_students = Student.objects.filter(marks__lte=35, marks__gte=30)

    for student in all_students:
        student.marks = student.marks+7
        student.save()

    all_classzes1 = Classz.objects.filter(pk=1)
    all_classzes2 = Classz.objects.filter(pk=2)
    all_classzes3 = Classz.objects.filter(pk=3)
    all_classzes4 = Classz.objects.filter(pk=4)

    all_students_in_classz1 = Student.objects.filter(classz_id=1)
    all_students_in_classz2 = Student.objects.filter(classz_id=2)
    all_students_in_classz3 = Student.objects.filter(classz_id=3)
    all_students_in_classz4 = Student.objects.filter(classz_id=4)

    template = loader.get_template('student/face.html')
    context = {
        'all_classzes1': all_classzes1,
        'all_classzes2': all_classzes2,
        'all_classzes3': all_classzes3,
        'all_classzes4': all_classzes4,

        'all_students_in_classz1': all_students_in_classz1,
        'all_students_in_classz2': all_students_in_classz2,
        'all_students_in_classz3': all_students_in_classz3,
        'all_students_in_classz4': all_students_in_classz4
    }
    return HttpResponse(template.render(context, request))








