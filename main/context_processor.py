# Define custom context for base.html

from main.models import Subject, Course, CourseVideo, Comment
from user.models import Profile


def custom_context(request):
    subjects = Subject.objects.all()
    courses = Course.objects.all()
    videos = CourseVideo.objects.all()
    comments = Comment.objects.all()
    profile = Profile.objects.all()
    return {
        'subjects': subjects,
        'courses': courses,
        'videos': videos,
        'comments': comments,
        'profile': profile
    }