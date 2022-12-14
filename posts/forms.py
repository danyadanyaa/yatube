from django import forms
from .models import *


class NewPost(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].empty_label = 'Без группы'

    class Meta:
        model = Post
        fields = ('text', 'group', 'image')
        widgets = {
            'text': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
        }
    #content = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}), label='Ваш пост', required=True)
    #group = forms.ModelChoiceField(queryset=Group.objects.all(), label='Группа', required=False, empty_label='Без группы')


class CommentAdd(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', ]

