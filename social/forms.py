from django import forms

from social.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('caption','image','tags')