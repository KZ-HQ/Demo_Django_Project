from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Subject(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    slug = models.SlugField()

    def __str__(self):
        return f'{self.title}'


class Course(models.Model):
    # One to many relationship with Subject model
    # If a Subject is deleted, the corresponding Courses will also be deleted
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    # One to many relationship with User model
    # If a User is deleted, the corresponding Courses will also be deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)
    teacher = models.CharField(max_length=100, default='Unknown')
    description = models.TextField(null=False)
    source_link = models.TextField(default="No Source")

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    # One to many relationship with User model
    # If a User is deleted, the corresponding Comments will also be deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # One to many relationship with Course model
    # If a Course is deleted, the corresponding Comments will also be deleted
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    comment = models.TextField(null=False)

    def __str__(self):
        return f'{self.comment} in {self.course}'


class CourseVideo(models.Model):
    # One to many relationship with Course model
    # If a Course is deleted, the corresponding Course Videos will also be deleted
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    teacher = models.CharField(max_length=100, default='Unknown')
    link = models.CharField(max_length=11, null=False)

    def __str__(self):
        return f'<<{self.title}>> From <<{self.course}>>'
