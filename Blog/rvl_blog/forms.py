from django import forms
from rvl_blog.models import Post, Comments


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'customtextclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['author', 'text']

        widgets = {
            'author': forms.TextInput(attrs={'class': 'customtextclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }
