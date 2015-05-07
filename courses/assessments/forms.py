from django import forms

# SOME_CHOICES = (
# ('yes', 'Yes'), ('no', 'No'), ('cancelled', 'Cancelled'),
# )


# class AnswerCheckBoxSelectMultiple():
#     """
#     For fixing bad labels
#     """
#     def __init__(self, question_id, *args, **kwargs):
#         self.question_id = question_id
#         super(AnswerCheckBoxSelectMultiple, self).__init__(*args, **kwargs)
#
#     def id_for_label(self, id_):
#         if id_:
#             id_ += str(self.question_id+100500)
#         return id_


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