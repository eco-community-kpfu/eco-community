from django import forms
from app_blog.models import Comment, Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'text', 'image', 'topics')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control mb-3'}),
            'topics': forms.CheckboxSelectMultiple(),
        }


class CommentForm(forms.ModelForm):
    comment = forms.CharField(label="", widget=forms.Textarea(attrs={'rows': '1', }))

    class Meta:
        model = Comment
        fields = ('comment',)
