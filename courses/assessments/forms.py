from django import forms


class QuestionForm(forms.Form):
    def __init__(self, text, number, answers, *args, **kwargs):
        self.text = text
        self.number = number
        answers = tuple(("%d-%d" % (number, answer.number), answer.text) for answer in answers)
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields["answers"] = forms.MultipleChoiceField(choices=answers,
                                                           widget=forms.CheckboxSelectMultiple(
                                                               attrs={"id": unicode(number)}
                                                           ))