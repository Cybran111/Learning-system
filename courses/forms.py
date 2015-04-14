__author__ = 'cybran'
from django import forms

from courses.models import Course, Lecture


class NewLectureForm(forms.ModelForm):
    class Meta:
        error_css_class = 'has-error'
        model = Lecture
        fields = ['title', 'video_url', ]
        labels = {'title': 'Title', 'video_url': 'Video lecture URL', }

        widgets = {'title': forms.TextInput(attrs={'placeholder': 'Enter title', 'class': 'form-control'}),

                   'video_url': forms.URLInput(attrs={'placeholder': 'Enter URL to the lecture (only YouTube allowed)',
                                                      'class': 'form-control'}), }

        error_messages = {'video_url': {'invalid': "Only videos from YouTube are allowed.", }, }


class NewCourseForm(forms.ModelForm):
    title = forms.CharField(label="Title", widget=forms.TextInput(
        attrs={'placeholder': 'Enter the title of the course', 'class': 'form-control'}))
    short_desc = forms.CharField(label='Short description', widget=forms.TextInput(
        attrs={'placeholder': 'Enter the short description of the course', 'class': 'form-control'}))
    full_desc = forms.CharField(label="Full description", widget=forms.Textarea(
        attrs={'placeholder': 'Enter the full description of the course', 'class': 'form-control'}))

    class Meta:
        model = Course
        fields = ('title', 'short_desc', 'full_desc')