from django.contrib import admin
from .models import (
    Subject,
    Course,
    CourseVideo,
    Comment
)
# Register your models here.

# admin.site.register(Subject)


@admin.register(Subject)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Course)
admin.site.register(CourseVideo)
admin.site.register(Comment)
