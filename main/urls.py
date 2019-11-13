from django.urls import path
from .views import (
    IndexListView,
    SubjectDetailView,
    CourseDetailView,
    CommentCreateView,
    CourseVideoDetailView,
    about
)


urlpatterns = [
    # about route
    path('about/', about, name='main-about'),
    path('subject/<slug:slug>/', SubjectDetailView.as_view(), name='main-subjects'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='main-course'),
    path('course/<int:pk>/comment/', CommentCreateView.as_view(), name='main-comment'),
    path('course/<int:pk>/video/<int:video_pk>/', CourseVideoDetailView.as_view(), name='main-video'),
    # index route
    path('', IndexListView.as_view(), name='main-index')

]