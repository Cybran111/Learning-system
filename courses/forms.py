__author__ = 'cybran'
from django import forms

from models import Course


class NewCourseForm(forms.ModelForm):
    title = forms.CharField(label="Title",
                            widget=forms.TextInput(attrs={
                                'placeholder': 'Enter the title of the course',
                                'class': 'form-control'
                            }
                            )
    )
    short_desc = forms.CharField(label='Short description',
                                 widget=forms.TextInput(attrs={
                                     'placeholder': 'Enter the short description of the course',
                                     'class': 'form-control'
                                 }
                                 )
    )
    full_desc = forms.CharField(label="Full description",
                                widget=forms.Textarea(attrs={
                                    'placeholder': 'Enter the full description of the course',
                                    'class': 'form-control'
                                }
                                )
    )

    class Meta:
        model = Course
        fields = ('title', 'short_desc', 'full_desc')