from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from crm.models import Student, Course


def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

def details(request):
    id = request.GET.get('id')
    student = Student.objects.get(pk=id)
    return render(request, 'details.html', {'student': student})

def add(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        return render(request, 'add.html', {'courses': courses})
    if request.method == 'POST':
        name = request.POST.get('name', '')
        surname = request.POST.get('surname', '')
        course_id = request.POST.get('course_id', '')

        if name == '' or surname == '':
            messages.add_message(request, messages.ERROR, 'Заполните все поля!')
            return redirect('/add')

        student = Student()
        student.name = name
        student.surname = surname

        if course_id != '':
            course = Course.objects.get(pk=course_id)
            student.course = course
        else:
            student.course = None
        student.save()

        return redirect('/student?id={}'.format(student.id))

def edit(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        student = Student.objects.get(pk=id)
        return render(request, 'edit.html', {'student': student})
    if request.method == 'POST':
        name = request.POST.get('name', '')
        surname = request.POST.get('surname', '')

        id = request.GET.get('id')

        if name == '' or surname == '':
            return HttpResponse("Заполните все поля")

        student = Student.objects.get(pk=id)
        student.name = name
        student.surname = surname
        student.save()

        return redirect('/student?id={}'.format(student.id))

def delete(request):
    id = request.GET.get('id')
    student = Student.objects.get(pk=id)
    student.delete()

    return redirect('/')