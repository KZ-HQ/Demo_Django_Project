from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import Subject, Course, Comment, CourseVideo
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


# about page function based view
def about(request):
    return render(request, 'main/about.html', {'title': 'About'})


# IndexListView class based view
class IndexListView(ListView):
    model = Subject
    template_name = 'main/index.html'
    context_object_name = 'subjects'
    ordering = ['title']
    extra_context = {'title': 'Index'}


# SubjectListView class based view
class SubjectDetailView(DetailView):
    model = Subject
    context_object_name = 'subject'
    extra_context = {'title': 'Subjects'}


class CourseDetailView(DetailView):
    model = Course
    template_name = "main/course_detail.html"
    context_object_name = 'course'
    extra_context = {
        'title': 'Course Detail'
    }


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['comment']
    template_name = 'main/comment_form.html'

    def get_success_url(self):
        return reverse('main-course', kwargs={'pk': self.object.course.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.course = Course.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)


class CourseVideoDetailView(DetailView):
    model = CourseVideo
    template_name = "main/course_videos.html"
    context_object_name = 'videos'
    extra_context = {
        'title': 'Course Lecture'
    }

    def get_context_data(self, **kwargs):
        context = super(CourseVideoDetailView, self).get_context_data(**kwargs)
        video_pk = CourseVideo.objects.get(id=self.kwargs.get('video_pk'))
        context['video_pk'] = video_pk
        return context
