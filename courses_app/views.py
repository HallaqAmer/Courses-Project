from django.shortcuts import render,redirect
from django.contrib import messages
from . import models
from .models import Course,Desc

def display_home(request):

    context= {
        "courses": models.get_all_courses()
    }
    return render(request,"index.html",context)

def add_course(request):

    if request.method == "POST":
        errors=Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            description=models.create_description(request.POST)
            new_course=models.create_course(request.POST,description)
            return redirect("/")

def display_deletepage(request):
    if request.method=="POST":
        courseid=request.POST['courseid']
        print(courseid)
        request.session['courseid']=courseid
        return redirect("/course/destroy")

def delete_course(request):
    
    courseid=request.session['courseid']
    print(courseid)
    course=Course.objects.get(id=courseid)
    context = {
    "course": course
    }
    return render(request,"course_del.html",context)

def confirm_course_removal(request):

    if request.method=="POST":
        courseid=request.session['courseid']
        models.delete_course(request.POST,courseid)
        del request.session['courseid']
        return redirect("/")

def redirct_comments(request):
    if request.method=="POST":
        request.session['courseid']=request.POST['courseid']
        return redirect('/comments')

def display_comments(request):

    id=request.session['courseid']
    course=Course.objects.get(id=id)
    comments=course.comments.all()
    context= {
        "comments": comments
    }

    return render(request,"comment.html",context)

def add_comments(request):
    
    if request.method=="POST":
        courseid=request.session['courseid']
        print(courseid)
        comment=models.create_comment(request.POST,courseid)
        return redirect('/comments')

def root_button(request):
    if request.method=="POST":
        return redirect('/')



