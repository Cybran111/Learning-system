from django import forms

# SOME_CHOICES = (
# ('yes', 'Yes'), ('no', 'No'), ('cancelled', 'Cancelled'),
# )


class QuestionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        answers = kwargs.pop('answers')
        answers = tuple((answer.number, answer.text) for answer in answers)
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields["answers"] = forms.MultipleChoiceField(choices=answers, widget=forms.CheckboxSelectMultiple())