from django import forms
from app_blog.models import Comment


class CommentForm(forms.ModelForm):
    comment = forms.CharField(label="", widget=forms.Textarea(attrs={'rows': '1', }))

    class Meta:
        model = Comment
        fields = ('comment',)
