from django.db import models
from datetime import datetime

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Course name should be more than 5 characters"
        if len(postData['description']) < 15:
            errors["description"] = "Description should be more than 15 characters"
        
        return errors

class Desc(models.Model):
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = CourseManager()


class Course(models.Model):
    name=models.CharField(max_length=255)
    desc=models.OneToOneField(Desc,related_name="courses",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = CourseManager()

class Comment(models.Model):
    content=models.TextField()
    name=models.CharField(max_length=255)
    course=models.ForeignKey(Course,related_name="comments", on_delete=models.CASCADE,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = CourseManager()

def create_course(postData,description):
    name=postData['name']
    desc=description
    return Course.objects.create(name=name,desc=desc)

def create_description(postData):
    
    content=postData['description']
    return Desc.objects.create(content=content)

def get_all_courses():
    return Course.objects.all()

def delete_course(postData,courseid):

    if postData['answer'] == "yes":
        course=Course.objects.get(id=courseid)
        course.delete()

def create_comment(postData,courseid):
    name=postData['name']
    content=postData['content']
    course=Course.objects.get(id=courseid)
    print(courseid)
    return Comment.objects.create(name=name,content=content,course=course)

def get_all_comments():
    return Comment.objects.all()

