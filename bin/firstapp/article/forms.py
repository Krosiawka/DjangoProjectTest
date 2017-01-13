# -*- coding: utf-8 -*-

from django.forms import ModelForm
from article.models import Comments
from django import forms

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']
        widgets = {
            'comments_text': forms.Textarea(attrs={"class": "mdl-textfield__input", "type": "text", "rows": "5", "id": "sample5"}),          
        }